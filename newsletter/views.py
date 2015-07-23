import csv
import tempfile
import pygal

from decimal import Decimal
from django.shortcuts import render
from newsletter import forms, tasks, models

from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView

from django.db.models import Count

from django.shortcuts import render_to_response

from django.http import HttpResponse,StreamingHttpResponse

from braces.views import LoginRequiredMixin, SuperuserRequiredMixin


class TaskRunnerView(SuperuserRequiredMixin,FormView):
    def form_valid(self, form):
        csv_form = form.cleaned_data["csv_file"]
        f = tempfile.NamedTemporaryFile(delete=False)
        for chunk in csv_form.chunks():
            f.write(chunk)
        print(self.task)
        self.task.delay(f.name, form.cleaned_data['date'])
        return super(TaskRunnerView, self).form_valid(form)


class UploadSubscribersView(TaskRunnerView):
    template_name = 'newsletter/subscribers_upload_view.html'
    form_class = forms.UploadSubscribersInput
    success_url = '/'
    task = tasks.load_active_subscribers


class ActiveSubscribersView(LoginRequiredMixin,DetailView):
    model = models.Week


class WeekListView(LoginRequiredMixin,ListView):
    model = models.Week

class Echo(object):
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


def csv_response(signups):
    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)
    response = StreamingHttpResponse((writer.writerow(row) for row in signups),
                                    content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    return response

def histogram_response(signups):
    bar_chart = pygal.Bar()
    bar_chart.title = 'Signups by Affiliate Code'
    bar_chart.x_labels = ''
    for signup in signups:
        bar_chart.add(signup['group'], [signup['count']])
    bar_chart_svg = bar_chart.render()
    return HttpResponse(bar_chart_svg, content_type='image/svg+xml')


class SignupsReportView(LoginRequiredMixin,FormView):
    template_name = 'newsletter/signups_report_view.html'
    form_class = forms.SignupReportInput

    def form_valid(self, form):
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        signups = models.Signup.objects.filter(
            created__gte=start_date).filter(
                created__lte=end_date
            ).values_list('group')
        report_type = form.cleaned_data['report_type']
        if report_type == 'csv':
            signups = signups.values_list('group')
            return csv_response(signups)
        elif report_type == 'csv-count':
            signups = signups.values('group').annotate(
                    count=Count('group')).values_list('group', 'count')
            return csv_response(signups)
        elif report_type == 'html-count':
            signups = signups.values('group').annotate(
                    count=Count('group'))
            return render_to_response('newsletter/signup-report.html', {
                    'signups': signups,
                })
        elif report_type == 'svg':
            signups = signups.values('group').annotate(
                    count=Count('group'))
            return histogram_response(signups)


class LongevityReportView(LoginRequiredMixin,FormView):
    template_name = 'newsletter/signups_report_view.html'
    form_class = forms.LongevityInput

    def form_valid(self, form):
        start_date = form.cleaned_data['start_date']
        end_date = form.cleaned_data['end_date']
        signups = models.Signup.objects.filter(
            created__gte=start_date).filter(
                created__lte=end_date
            )
        signups = signups.extra(
            {"month": "date_trunc('month', created)"}
        ).values("month").annotate(count=Count("id")).order_by("month")
        active = signups.filter(pk__in=models.Subscriber.objects.filter(active=True))
        active_iter = active.iterator()
        a = next(active_iter)
        x_values = []
        y_values = []
        for c in signups:
            x_values.append(c['month'].strftime('%b %Y'))
            if c['month'] == a['month']:
                y_values.append(Decimal(a['count']) / Decimal(c['count']))
                try:
                    a = next(active_iter)
                except:
                    a = { 'month': '' }
            else:
                y_values.append(0)
        bar_chart = pygal.Bar()
        bar_chart.title = 'Signup Longevity Analysis'
        bar_chart.x_labels = x_values
        bar_chart.add('Total Signups', y_values)
        bar_chart_svg = bar_chart.render()
        return HttpResponse(bar_chart_svg, content_type='image/svg+xml')



class IndexPage(TemplateView):
    template_name = 'newsletter/index-page.html'
