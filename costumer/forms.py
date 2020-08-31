from django import forms
from .models import *


class FormCreateEditCustomer(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'firstname',
            'lastname',
            'phonenumber',
            'notes',
        ]