from django import forms
from .models import *


class Form_Create_Tweak_Customer(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'firstname',
            'lastname',
            'phonenumber',
            'notes',
        ]