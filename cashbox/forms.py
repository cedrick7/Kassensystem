from django import forms
from .models import *

styling = ""







#---------------------------------------------

class FormCreateReversalBill(forms.Form):
    amount = forms.DecimalField(required=True,
                                label='',
                                widget=forms.NumberInput(
                                    attrs={"placeholder": "",
                                           "class": ""
                                           }))
    # kasse automaisch, mitarbeiter automatisch, creation automatisch
    # Ready to style


CHOICES_PAYMENT = (
    ('cash', 'Barzahlung'),
    ('card', 'Kartenzahlung'),
    ('paypal', 'PayPal')
)


CHOICES_CUSTOMERS = (
    ('new', 'Neukunde'),
    ('customer_01', 'Vorname Nachname (Kunde 1)'),
    ('customer_02', 'Vorname Nachname (Kunde 2)')
)

CHOICES_FOUND = (
    ('random', 'Per Zufall'),
    ('website', 'Webseite'),
    ('facebook', 'Facebook')
)

CHOICES_RATING = (
    ('5', '5'),
    ('4', '4'),
    ('3', '3'),
    ('2', '2'),
    ('1', '1'),
)


class FormCart(forms.Form):
    payment = forms.CharField(
        required=True,
        label='rating',
        widget=forms.Select(
            choices=CHOICES_PAYMENT,
            attrs={
                'class': 'btn btn-primary button'
            }
        ),
    )


class FormGetInfo(forms.Form):
    customer = forms.ChoiceField(
        required=True,
        label='',
        choices=CHOICES_CUSTOMERS,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )
    found = forms.ChoiceField(
        required=True,
        label='',
        choices=CHOICES_FOUND,
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )
    rating = forms.CharField(
        required=True,
        label='rating',
        widget=forms.RadioSelect(
            choices=CHOICES_RATING,
            attrs={
            }
        ),
    )
