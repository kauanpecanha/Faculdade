from django.shortcuts import render

# Create your views here.

from django.views.generic.edit import FormView

from main import forms

class ViewFaleConosco(FormView):
    template_name = "contactUs.html"
    form_class = forms.FormFaleConosco
    success_url = "/"