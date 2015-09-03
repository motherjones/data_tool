from django import forms
from newsletter import models


class UploadSubscribersInput(forms.Form):
    csv_file = forms.FileField()
    date = forms.DateField()
    notes = forms.CharField(widget=forms.Textarea)


class SignupReportInput(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()
    report_type = forms.ChoiceField(choices=(
                    ('csv', 'csv with just codes'),
                    ('csv-count', 'csv with codes and counts'),
                    ('html-count', 'html table of counts'),
                    ('svg', 'histogram of codes'),
                ))
    first_only = forms.BooleanField(label="First Signups Only",
                                    initial=False, required=False)


class LongevityInput(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()
    code = forms.CharField(required=False)
    by_group = forms.BooleanField(initial=True, required=False)


class ActiveSubscribersGraphInput(forms.Form):
    start_week = forms.ModelChoiceField(
                 queryset=models.Week.objects.all().order_by('date'))
    end_week = forms.ModelChoiceField(
               queryset=models.Week.objects.all().order_by('-date'))
