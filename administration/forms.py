from django import forms
from .models import *
from authorization.models import *
from analyzation.models import *
from cashbox.models import *
from costumer.models import *
from product.models import *



# Sortimentverwaltung

# Produkt/Dienstleistung
class FormCreateEditProducts(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'type',
            'brand',
            'costs',
            'tax',
            'weight',
            'picture',
            'discount',
        ]


# Eigenschaft
class FormCreateEditProperties(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'title',
        ]

# Kategorie
class FormCreateEditCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'title',
            'discount',
        ]

# discount
class FormCreateEditDiscount(forms.ModelForm):
    class Meta:
        model = Discount
        fields = [
            'amount', 
            # kasse automaisch, mitarbeiter automatisch, creation automatisch
        ]



# Mitarbeiterverwaltung

# Mitarbeiter
class FormCreateEditEmployee(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'firstname', 
            'lastname', 
            'role', 
            'password', 
            'picture' 
        ]



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