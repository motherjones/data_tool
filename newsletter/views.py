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
        print(self.request.FILES)
        records = csv.reader(self.request.FILES["csv_file"])
        records.__next__()
        truthy = { 'TRUE': True, 'FALSE' : False }
        for line in records:
            subscriber = models.Subscribers()
            subscriber.date = form.cleaned_data["date"]
            subscriber.bounce = line[0]
            subscriber.email = line[1]
            subscriber.active = truthy.get(line[2])
            subscriber.domain = line[3]
            subscriber.save()
        return super(UploadSubscribersView, self).form_valid(form)
