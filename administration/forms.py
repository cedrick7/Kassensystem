from django import forms
from .models import *
from authorization.models import *
from analyzation.models import *
from cashbox.models import *
from costumer.models import *
from product.models import *

styling = ""


choices = (
    ('cashier', 'Kassierer'),
    ('admin', 'Administrator'),
    ('analyst', 'Analyst')
)

# ----------------------------------------------------------------------------------------------------------------------
# forms von cedi als template

# Produkt anzeigen, bearbeiten, löschen
class FormProductDetail(forms.Form):
    title = forms.CharField(
        required = True,
        label = 'Produktname',
        initial = Product.title,
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Produktname",
                "class": "form-control needs-validation",
                "style": styling
            },
        )
    )
    # ... = ...

    class Meta:
        model = Product
        fields = ['title']


# Produkt anlegen
class FormProductCreate(forms.Form):
    title = forms.CharField(
        required = True,
        label = 'Prdouktname',
        # inital = "",
        widget = forms.TextInput(
            attrs = {
                "placeholder": "Produktname",
                "class": "form-control needs-validation",
                "style": styling
            }
        )
    )

    # ... = ...

    class Meta:
        model = Product
        fields = ['title']

# ----------------------------------------------------------------------------------------------------------------------











# Sortimentverwaltung

# Produkt/Dienstleistung
class FormCreateEditProducts(forms.Form):
    title = forms.CharField(required = True,
        label = '',
        widget = forms.TextInput(
            attrs = {"placeholder": "",
                     "class": ""
                    }))

    #category = forms.ManyToManyField(Category, blank=True)

    description = forms.CharField(required = True,
        label = '',
        widget = forms.TextInput(
            attrs = {"placeholder": "",
                     "class": ""
                    }))
    costs = forms.DecimalField(required = True,
        label = '',
        widget = forms.NumberInput(
            attrs = {"placeholder": "",
                     "class": ""
                    }))
    weight = forms.DecimalField(required = True,
        label = '',
        widget = forms.NumberInput(
            attrs = {"placeholder": "",
                     "class": ""
                    }))  # in Gramm
    stock = forms.IntegerField(required = True,
        label = '',
        widget = forms.NumberInput(
            attrs = {"placeholder": "",
                     "class": ""
                    }))
    brand = forms.CharField(required = True,
        label = '',
        widget = forms.TextInput(
            attrs = {"placeholder": "",
                     "class": ""
                    }))

    #tax = forms.ForeignKey(Tax, on_delete=models.CASCADE, blank=True, default=None, null=True)
    #discount = forms.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, default=None, null=True)

    picture = forms.FileField(required = True,
        label = '',
        widget = forms.FileInput(
            attrs = {"placeholder": "",
                     "class": ""
                    }))

    #property = forms.ManyToManyField(Property, blank=True)


# Eigenschaft
class FormCreateEditProperties(forms.Form):
    title = forms.CharField(required=True,
                            label='',
                            widget=forms.TextInput(
                                attrs={"placeholder": "",
                                       "class": ""
                                       }))

# Kategorie
class FormCreateEditCategory(forms.Form):
    title = forms.CharField(required=True,
                            label='',
                            widget=forms.TextInput(
                                attrs={"placeholder": "",
                                       "class": ""
                                       }))
  #  discount = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, default=None, null=True)

# discount
class FormCreateEditDiscount(forms.Form):

       discount = forms.DecimalField(required = True,
        label = '',
        widget = forms.NumberInput(
            attrs = {"placeholder": "",
                     "class": ""
                    }))
#Is this right?


# Mitarbeiterverwaltung

# Mitarbeiter
class FormCreateEditEmployee(forms.Form):
    firstname = forms.CharField(required = True,
        label = '',
        widget = forms.TextInput(
            attrs = {"placeholder": "",
                     "class": ""
                    }))

    lastname = forms.CharField(required = True,
        label = '',
        widget = forms.TextInput(
            attrs = {"placeholder": "",
                     "class": ""
                    }))

    email = forms.EmailField(required = True,
        label = '',
        widget = forms.EmailInput(
            attrs = {"placeholder": "",
                     "class": ""
                    }))

    role = forms.CharField(required = True,
        label = '',
        widget = forms.TextInput(
            attrs = {"placeholder": "",
                     "class": ""
                    }))

    phone_number = forms.DecimalField(required = True,
        label = '',
        widget = forms.NumberInput(
            attrs = {"placeholder": "",
                     "class": ""
                    }))

    work_since = forms.DateField(required = True,
        label = '',
        widget = forms.DateInput(
            attrs = {"placeholder": "",
                     "class": ""
                    }))

    img = forms.FileField(required = True,
        label = '',
        widget = forms.FileInput(
            attrs = {"placeholder": "",
                     "class": ""
                    }))
    #color = Color field (not in Models)
    #is_favourite= Form for boolean checkbox (not in models)



# Systemverwaltung

# Backup
class FormCreateEditBackup(forms.Form):
    title = forms.CharField(required = True,
        label = '',
        widget = forms.TextInput(
            attrs = {"placeholder": "",
                     "class": ""
                    }))

    creation = forms.DateTimeField(required = True,
        label = '',
        widget = forms.DateInput(
            attrs = {"placeholder": "",
                     "class": ""
                    }))

    store = forms.FileField(required = True,
        label = '',
        widget = forms.FileInput(
            attrs = {"placeholder": "",
                     "class": ""
                    }))

    comment = forms.CharField(required = True,
        label = '',
        widget = forms.TextInput(
            attrs = {"placeholder": "",
                     "class": ""
                    }))

    #employee = forms.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, default=None)


# Safe
class FormCreateEditSafe(forms.Form):
    title = forms.CharField(required=True,
                             label='',
                             widget=forms.TextInput(
                                 attrs={"placeholder": "",
                                        "class": ""
                                        }))

    amount = forms.DecimalField(required=True,
                                 label='',
                                 widget=forms.NumberInput(
                                     attrs={"placeholder": "",
                                            "class": ""
                                            }))

# Zahlungsmittel
class FormCreateEditPayment(forms.Form):
    title = forms.CharField(required=True,
                                 label='',
                                 widget=forms.TextInput(
                                     attrs={"placeholder": "",
                                            "class": ""
                                            }))

    picture = forms.FileField(required=True,
                                 label='',
                                 widget=forms.FileInput(
                                     attrs={"placeholder": "",
                                            "class": ""
                                            }))

# Kassen
class FormCreateEditCashbox(forms.Form):
    title = forms.CharField(required=True,
                             label='',
                             widget=forms.TextInput(
                                 attrs={"placeholder": "",
                                        "class": ""
                                        }))

    amount = forms.DecimalField(required=True,
                                 label='',
                                 widget=forms.NumberInput(
                                     attrs={"placeholder": "",
                                            "class": ""
                                            }))

# Kunden
# siehe Kundenverwaltung

class FormEmployeeCreateEdit(forms.Form):
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

    email = forms.EmailField(required=True,
                             label='',
                             widget=forms.EmailInput(
                                 attrs={"placeholder": "",
                                        "class": ""
                                        }))

    phone_number = forms.CharField(required=True,
                             label='',
                             widget=forms.NumberInput(
                                 attrs={"placeholder": "",
                                        "class": ""
                                        }))

    work_since = forms.DateTimeField(required=True,
                             label='',
                             widget=forms.DateInput(
                                 attrs={"placeholder": "",
                                        "class": ""
                                        }))

    role = forms.ChoiceField(
        required = True,
        label = 'Rolle auswählen',
        choices = choices,
        widget = forms.Select(
            attrs = {
                'class': 'form-control'
            }
        ))

    img = forms.FileField(required=True,
                             label='',
                             widget=forms.FileInput(
                                 attrs={"placeholder": "",
                                        "class": ""
                                        }))

#class FormAdministrationEdit(forms.Form):
