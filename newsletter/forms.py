from django import forms

class UploadSubscribersInput(forms.Form):
    csv_file = forms.FileField()
    date = forms.DateField()


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
