from django import forms

class UploadSubscribersInput(forms.Form):
    csv_file = forms.FileField()
    date = forms.DateField()
