from django import forms
from .models import *


class FormCreateReversalBill(forms.ModelForm):
    class Meta:
        model = Bill_Product
        fields = [
            'amount', 
            # kasse automaisch, mitarbeiter automatisch, creation automatisch
        ]