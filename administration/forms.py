from django import forms
from .models import *
from authorization.models import *
from analyzation.models import *
from cashbox.models import *
from costumer.models import *
from product.models import *

styling = ""


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
class FormCreateEditBackup(forms.ModelForm):
    class Meta:
        model = Backup
        fields = [
            'title',
            'store',
            'creation',
            'comment',
            # mitarbeiter automatisch
        ]


# Safe
class FormCreateEditSafe(forms.ModelForm):
    class Meta:
        model = Safe
        fields = [
            'title',
            'amount',
        ]

# Zahlungsmittel
class FormCreateEditPayment(forms.ModelForm):
    class Meta:
        model = Paymenttool
        fields = [
            'title',
            'picture',
        ]

# Kassen
class FormCreateEditCashbox(forms.ModelForm):
    class Meta:
        model = Cashbox
        fields = [
            'title',
            'amount',
        ]

# Kunden
# siehe Kundenverwaltung

class FormEmployeeCreateEdit(forms.ModelForm):
    class Meta:
        model = Request
        fields = [
            'firstname',
            'lastname',
            'role',
            'password'
            # type automaisch, username automatisch
            # Administrator erstellt, bearbeitet, löscht employee
        ]