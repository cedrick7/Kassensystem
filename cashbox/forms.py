from django import forms
from .models import *
styling = ""

class FormCreateReversalBill(forms.Form):
    amount = forms.IntegerField(widget=forms.TextInput(attrs={"class": "form-row"}))
            # kasse automaisch, mitarbeiter automatisch, creation automatisch
            #Ready to style