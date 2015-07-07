import tempfile
from django.shortcuts import render
from newsletter import forms, tasks, models

from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView
from django.views.generic import DetailView


class UploadSubscribersView(FormView):
    template_name = 'newsletter/subscribers_upload_view.html'
    form_class = forms.UploadSubscribersInput
    success_url = '/'

    def form_valid(self, form):
        csv_form = form.cleaned_data["csv_file"]
        f = tempfile.NamedTemporaryFile(delete=False)
        for chunk in csv_form.chunks():
            f.write(chunk)
        tasks.load_active_subscribers.delay(f.name, form.cleaned_data['date'])
        return super(UploadSubscribersView, self).form_valid(form)


class ActiveSubscribersView(DetailView):
    model = models.Week

