from django import forms
from .models import *


class FormCreateReversalBill(forms.Form):
    model = Bill_Product
    amount = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-row"}))
            # kasse automaisch, mitarbeiter automatisch, creation automatisch
            #Ready to style