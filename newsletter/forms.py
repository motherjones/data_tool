import csv
from django import forms
from newsletter import models

class UploadSubscribersInput(forms.Form):
    csv_file = forms.FileField()
    date = forms.DateField()

    def save(self):
        records = csv.reader(self.cleaned_data["csv_file"])
        records.__next__()
        for line in records:
            subscriber = model.Subscribers()
            subscriber.date = self.cleaned_data["date"]
            subscriber.bounce = line[0]
            subscriber.email = line[1]
            truthy = { 'TRUE': True, 'FALSE' : False }
            subscriber.active = truthy.get(line[2])
            subscriber.domain = line[3]
            subscriber.save()
