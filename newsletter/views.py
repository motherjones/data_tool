import csv

from django.shortcuts import render
from newsletter import forms, models

from django.core.urlresolvers import reverse
from django.views.generic.edit import FormView


class UploadSubscribersView(FormView):
    template_name = 'newsletter/subscribers_upload_view.html'
    form_class = forms.UploadSubscribersInput
    success_url = '/'

    def form_valid(self, form):
        csv_form = form.cleaned_data["csv_file"]
        csv_stream = TextIOWrapper(BytesIO(csv_form.read()))
        records = csv.reader(csv_stream)
        records.__next__()
        truthy = { 'true': True, 'false' : False }
        for line in records:
            try:
                subscriber = models.Subscribers()
                subscriber.date = form.cleaned_data["date"]
                subscriber.bounces = line[0]
                subscriber.email = line[1]
                subscriber.active = truthy.get(line[2])
                subscriber.domain = line[3]
                subscriber.save()
            except:
                pass
        return super(UploadSubscribersView, self).form_valid(form)
