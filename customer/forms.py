from django import forms
from .models import Customer    
styling = ""

class FormCreateEditCustomer(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['firstname', 'lastname', 'phonenumber', 'notes']

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


