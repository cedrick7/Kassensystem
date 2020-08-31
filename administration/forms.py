from django import forms
from .models import *
from authorization.models import *
from analyzation.models import *
from cashbox.models import *
from costumer.models import *
from product.models import *



# Sortimentverwaltung

# Produkt/Dienstleistung
class Form_Create_Tweak_Products(forms.ModelForm):
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
class Form_Create_Tweak_Propertys(forms.ModelForm):
    class Meta:
        model = Property
        fields = [
            'title',
        ]

# Kategorie
class Form_Create_Tweak_Categorie(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'title',
            'discount',
        ]

# discount
class Form_Create_Tweak_Discount(forms.ModelForm):
    class Meta:
        model = Discount
        fields = [
            'amount', 
            # kasse automaisch, mitarbeiter automatisch, creation automatisch
        ]



# Mitarbeiterverwaltung

# Mitarbeiter
class Form_Create_Tweak_Employee(forms.ModelForm):
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
class Form_Create_Tweak_Backup(forms.ModelForm):
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
class Form_Create_Tweak_Safe(forms.ModelForm):
    class Meta:
        model = Safe
        fields = [
            'title',
            'amount',           
        ]

# Zahlungsmittel
class Form_Create_Tweak_Payment(forms.ModelForm):
    class Meta:
        model = Paymenttool
        fields = [
            'title',
            'picture',
           
        ]

# Kassen
class Form_Create_Tweak_Cashbox(forms.ModelForm):
    class Meta:
        model = Cashbox
        fields = [
            'title',
            'amount',
        ]

# Kunden
# siehe Kundenverwaltung