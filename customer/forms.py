from django import forms
from .models import *
styling = ""

class FormCreateEditCustomer(forms.ModelForm):
        firstname = forms.CharField(required=True,
                             label='',
                             widget=forms.TextInput(
                                 attrs={"placeholder": "",
                                        "class": ""
                                        }))
        lastname = forms.CharField(required=True,
                             label='',
                             widget=forms.TextInput(
                                 attrs={"placeholder": "",
                                        "class": ""
                                        }))
        phone_number = forms.CharField(required=True,
                             label='',
                             widget=forms.NumberInput(
                                 attrs={"placeholder": "",
                                        "class": ""
                                        }))
        notes = forms.CharField(required=True,
                             label='',
                             widget=forms.TextInput(
                                 attrs={"placeholder": "",
                                        "class": ""
                                        }))
