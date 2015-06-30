from django.shortcuts import render
from newsletter import forms

from django.views.generic.edit import FormView


class UploadSubscribersView(FormView):
    template_name = 'newsletter/subscribers_upload_view.html'
    form_class = forms.UploadSubscribersInput
