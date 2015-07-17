from django import forms

class UploadSubscribersInput(forms.Form):
    csv_file = forms.FileField()
    date = forms.DateField()


class SignupReportInput(forms.Form):
    start_date = forms.DateField()
    end_date = forms.DateField()
