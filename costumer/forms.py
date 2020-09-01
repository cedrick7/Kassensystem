from django import forms
from .models import *


class FormCreateEditCustomer(forms.ModelForm):
        model = Customer
        firstname = forms.CharField(max_length=45, required=False, widget=forms.TextInput(attrs={"class": "form-row"}))
        lastname = forms.CharField(max_length=45, required=False, widget=forms.TextInput(attrs={"class": "form-row"}))
        phonenumber = forms.CharField(max_length=45, required=False, widget=forms.TextInput(attrs={"class": "form-row"}))
        notes = forms.CharField(widget=forms.TextInput(attrs={"class": "form-row"}))
