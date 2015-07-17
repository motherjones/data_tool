import csv
import tempfile
from django.shortcuts import render
from newsletter import forms, tasks, models

from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.views.generic import DetailView, ListView

from django.http import StreamingHttpResponse

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
        pseudo_buffer = Echo()
        writer = csv.writer(pseudo_buffer)
        response = StreamingHttpResponse((writer.writerow(row) for row in signups),
                                        content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        return response
