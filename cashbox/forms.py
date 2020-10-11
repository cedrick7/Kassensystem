from django import forms
from .models import *
styling = ""

class FormCreateReversalBill(forms.Form):
    amount = forms.DecimalField(required=True,
                                 label='',
                                 widget=forms.NumberInput(
                                     attrs={"placeholder": "",
                                            "class": ""
                                            }))
            # kasse automaisch, mitarbeiter automatisch, creation automatisch
            #Ready to style