import tempfile
from django.shortcuts import render
from newsletter import forms, tasks, models

from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.views.generic import DetailView, ListView

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
