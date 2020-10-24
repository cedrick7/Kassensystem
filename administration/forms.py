from django import forms
from .models import *
from authorization.models import *
from analyzation.models import *
from cashbox.models import *
from customer.models import *
from product.models import *
from authorization.models import *

styling = ''

choices = (
    ('cashier', 'Kassierer'),
    ('admin', 'Administrator'),
    ('analyst', 'Analyst')
)




class AttributeModelForm(forms.ModelForm):



class BackupModelForm(forms.ModelForm):
    class Meta:
        model = Backup
        fields = [
            'title',
            'comment',
            'creation',
            'employee', 
        ]      

class CashboxModelForm(forms.ModelForm):
    class Meta:
        model = Cashbox
        fields = [
            'title',
            'amount'
        ]

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'title',
            'color',
            'discount',
        ]

class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'firstname', 
            'lastname',
            'birthday',
            'email',
            'phonenumber',
        ]         

class DiscountModelForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = [
            'title', 
            'factor',
            'amount',
            'begin',
            'end',
        ]

class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'firstname',
            'lastname',
            'password',
            'picture',
            'role',
        ]                 

class PaymenttoolModelForm(forms.ModelForm):
    class Meta:
        model = Paymenttool
        fields = [
            'title',
            'path',
        ]      

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'type',
            'title',
            'category',
            'description',
            'costs',
            'weight',
            'stock',
            'brand',
            'tax',
            'discount',
            'path',
            'attributes',
        ]

class SafeModelForm(forms.ModelForm):
    class Meta:
        model = Safe
        fields = [
            'title',
            'amount'
        ]                 

class TaxModelForm(forms.ModelForm):
    class Meta:
        model = Tax
        fields = [
            'title',
            'taxrate', 
        ]


class BillModelForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = [
            'creation',
            'totalcosts',
            'employee',
            'cashbox',
            'paymenttool',
            'discount',
            'path', 
        ]  

class ReversalBillModelForm(forms.ModelForm):
    class Meta:
        model = ReversalBill
        fields = [
            'bill',
            'creation',
            'refund',
            'employee',
            'cashbox',
            'path', 
        ]      
    
class WorkTimeModelForm(forms.ModelForm):
    class Meta:
        model = Worktime
        fields = [
            'employee',
            'begin',
            'end',
        ]                 










# ----------------------------------------------------------------------------------------------------------------------
# forms von cedi als template

# # Produkt anzeigen, bearbeiten, löschen
# class FormProductDetail(forms.Form):
#     title = forms.CharField(
#         required=True,
#         label='Produktname',
#         initial=Product.title,
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Produktname',
#                 'class': 'form-control needs-validation',
#                 'style': styling,
#                 'name': 'productname'
#             }
#         )
#     )

#     # ... = ...

#     class Meta:
#         model = Product
#         fields = ['title']


# # Produkt anlegen
# class FormProductCreate(forms.Form):
#     title = forms.CharField(
#         required=True,
#         label='Prdouktname',
#         # inital = '',
#         widget=forms.TextInput(
#             attrs={
#                 'placeholder': 'Produktname',
#                 'class': 'form-control needs-validation',
#                 'style': styling
#             }
#         )
#     )

#     # ... = ...

#     class Meta:
#         model = Product
#         fields = ['title']


# # ----------------------------------------------------------------------------------------------------------------------


# # Sortimentverwaltung

# # Produkt
# class FormCreateEditProducts(forms.Form):
#     title = forms.CharField(required=True,
#                             label='Produktname',
#                             widget=forms.TextInput(
#                                 attrs={
#                                     'placeholder': 'Produktname',
#                                     'class': 'form-control needs-validation',
#                                     'style': styling,
#                                     'name': 'product_title',
#                                     'value': ''
#                                 }
#                             ))
#     description = forms.CharField(required=True,
#                                   label='Produktbeschreibung',
#                                   widget=forms.TextInput(
#                                       attrs={
#                                           'placeholder': 'Produktbeschreibung',
#                                           'class': 'form-control needs-validation',
#                                           'style': styling,
#                                           'name': 'product_description',
#                                           'value': ''
#                                       }
#                                   ))
#     costs = forms.DecimalField(required=True,
#                                label='Preis',
#                                widget=forms.NumberInput(
#                                    attrs={
#                                        'placeholder': 'Preis',
#                                        'class': 'form-control needs-validation',
#                                        'style': styling,
#                                        'name': 'product_price',
#                                        'value': ''
#                                    }
#                                ))
#     category = forms.CharField(required=True,
#                                label='Kategorien',
#                                widget=forms.TextInput(
#                                    attrs={
#                                        'placeholder': 'Kategorien',
#                                        'class': 'form-control needs-validation',
#                                        'style': styling,
#                                        'name': 'product_categories',
#                                        'value': ''
#                                    }
#                                ))
#     attribute = forms.CharField(required=True,
#                                 label='Eigenschaften',
#                                 widget=forms.TextInput(
#                                     attrs={
#                                         'placeholder': 'Eigenschaften',
#                                         'class': 'form-control needs-validation',
#                                         'style': styling,
#                                         'name': 'product_attributes',
#                                         'value': ''
#                                     }
#                                 ))
#     weight = forms.DecimalField(required=True,
#                                 label='Gewicht',
#                                 widget=forms.NumberInput(
#                                     attrs={
#                                         'placeholder': 'Gewicht',
#                                         'class': 'form-control needs-validation',
#                                         'style': styling,
#                                         'name': 'product_weight',
#                                         'value': ''
#                                     }
#                                 ))  # in Gramm
#     stock = forms.IntegerField(required=True,
#                                label='Bestand',
#                                widget=forms.NumberInput(
#                                    attrs={
#                                        'placeholder': 'Bestand',
#                                        'class': 'form-control needs-validation',
#                                        'style': styling,
#                                        'name': 'product_stock',
#                                        'value': ''
#                                    }
#                                ))
#     brand = forms.CharField(required=True,
#                             label='Marke',
#                             widget=forms.TextInput(
#                                 attrs={
#                                     'placeholder': 'Marke',
#                                     'class': 'form-control needs-validation',
#                                     'style': styling,
#                                     'name': 'product_brand',
#                                     'value': ''
#                                 }
#                             ))
#     taxfactor = forms.IntegerField(required=True,
#                                    label='Mehrwertsteuersatz',
#                                    widget=forms.NumberInput(
#                                        attrs={
#                                            'placeholder': 'Mehrwertsteuersatz',
#                                            'class': 'form-control needs-validation',
#                                            'style': styling,
#                                            'name': 'product_taxfactor',
#                                            'value': ''
#                                        }
#                                    ))
#     discount = forms.IntegerField(required=True,
#                                   label='Rabatt',
#                                   widget=forms.NumberInput(
#                                       attrs={
#                                           'placeholder': 'Rabatt',
#                                           'class': 'form-control needs-validation',
#                                           'style': styling,
#                                           'name': 'product_discount',
#                                           'value': ''
#                                       }
#                                   ))
#     picture = forms.FileField(required=False,
#                               label='Bild',
#                               widget=forms.FileInput(
#                                   attrs={
#                                       'placeholder': 'Bild',
#                                       'class': 'input-img form-control needs-validation',
#                                       'style': styling,
#                                       'name': 'product_picture',
#                                       'value': ''
#                                   }
#                               ))


# # Dienstleistung
# class FormCreateEditServices(forms.Form):
#     title = forms.CharField(required=True,
#                             label='Dienstleistungsname',
#                             widget=forms.TextInput(
#                                 attrs={
#                                     'placeholder': 'Dienstleistungsname',
#                                     'class': 'form-control needs-validation',
#                                     'style': styling,
#                                     'name': 'services_title',
#                                     'value': ''
#                                 }
#                             ))
#     description = forms.CharField(required=True,
#                                   label='Dienstleistungsbeschreibung',
#                                   widget=forms.TextInput(
#                                       attrs={
#                                           'placeholder': 'Dienstleistungsbeschreibung',
#                                           'class': 'form-control needs-validation',
#                                           'style': styling,
#                                           'name': 'services_description',
#                                           'value': ''
#                                       }
#                                   ))
#     costs = forms.DecimalField(required=True,
#                                label='Preis',
#                                widget=forms.NumberInput(
#                                    attrs={
#                                        'placeholder': 'Preis',
#                                        'class': 'form-control needs-validation',
#                                        'style': styling,
#                                        'name': 'services_price',
#                                        'value': ''
#                                    }
#                                ))
#     category = forms.CharField(required=True,
#                                label='Kategorien',
#                                widget=forms.TextInput(
#                                    attrs={
#                                        'placeholder': 'Kategorien',
#                                        'class': 'form-control needs-validation',
#                                        'style': styling,
#                                        'name': 'services_categories',
#                                        'value': ''
#                                    }
#                                ))
#     attribute = forms.CharField(required=True,
#                                 label='Eigenschaften',
#                                 widget=forms.TextInput(
#                                     attrs={
#                                         'placeholder': 'Eigenschaften',
#                                         'class': 'form-control needs-validation',
#                                         'style': styling,
#                                         'name': 'services_attributes',
#                                         'value': ''
#                                     }
#                                 ))
#     weight = forms.DecimalField(required=True,
#                                 label='Gewicht',
#                                 widget=forms.NumberInput(
#                                     attrs={
#                                         'placeholder': 'Gewicht',
#                                         'class': 'form-control needs-validation',
#                                         'style': styling,
#                                         'name': 'services_weight',
#                                         'value': ''
#                                     }
#                                 ))  # in Gramm
#     stock = forms.IntegerField(required=True,
#                                label='Bestand',
#                                widget=forms.NumberInput(
#                                    attrs={
#                                        'placeholder': 'Bestand',
#                                        'class': 'form-control needs-validation',
#                                        'style': styling,
#                                        'name': 'services_stock',
#                                        'value': ''
#                                    }
#                                ))
#     brand = forms.CharField(required=True,
#                             label='Marke',
#                             widget=forms.TextInput(
#                                 attrs={
#                                     'placeholder': 'Marke',
#                                     'class': 'form-control needs-validation',
#                                     'style': styling,
#                                     'name': 'services_brand',
#                                     'value': ''
#                                 }
#                             ))
#     taxfactor = forms.IntegerField(required=True,
#                                    label='Mehrwertsteuersatz',
#                                    widget=forms.NumberInput(
#                                        attrs={
#                                            'placeholder': 'Mehrwertsteuersatz',
#                                            'class': 'form-control needs-validation',
#                                            'style': styling,
#                                            'name': 'services_taxfactor',
#                                            'value': ''
#                                        }
#                                    ))
#     discount = forms.IntegerField(required=True,
#                                   label='Rabatt',
#                                   widget=forms.NumberInput(
#                                       attrs={
#                                           'placeholder': 'Rabatt',
#                                           'class': 'form-control needs-validation',
#                                           'style': styling,
#                                           'name': 'services_discount',
#                                           'value': ''
#                                       }
#                                   ))
#     picture = forms.FileField(required=False,
#                               label='Bild',
#                               widget=forms.FileInput(
#                                   attrs={
#                                       'placeholder': 'Bild',
#                                       'class': 'input-img form-control needs-validation',
#                                       'style': styling,
#                                       'name': 'services_picture',
#                                       'value': ''
#                                   }
#                               ))


# # Kategorie
# class FormCreateEditCategory(forms.Form):
#     title = forms.CharField(required=True,
#                             label='Kategoriename',
#                             widget=forms.TextInput(
#                                 attrs={
#                                     'placeholder': 'Kategoriename',
#                                     'class': 'form-control needs-validation',
#                                     'style': styling,
#                                     'name': 'category_title',
#                                     'value': ''
#                                 }
#                             ))
#     discount = forms.DecimalField(required=True,
#                                   label='Rabatt',
#                                   widget=forms.NumberInput(
#                                       attrs={
#                                           'placeholder': 'Rabatt',
#                                           'class': 'form-control needs-validation',
#                                           'style': styling,
#                                           'name': 'category_discount',
#                                           'value': ''
#                                       }
#                                   ))


# # Eigenschaften
# class FormCreateEditProperties(forms.Form):
#     title = forms.CharField(required=True,
#                             label='Eigenschaft Name',
#                             widget=forms.TextInput(
#                                 attrs={
#                                     'placeholder': 'Eigenschaft Name',
#                                     'class': 'form-control needs-validation',
#                                     'style': styling,
#                                     'name': 'attributes_title',
#                                     'value': ''
#                                 }
#                             ))


# # Rabatt
# class FormCreateEditDiscount(forms.Form):
#     title = forms.CharField(required=True,
#                             label='Rabatt Name',
#                             widget=forms.TextInput(
#                                 attrs={
#                                     'placeholder': 'Rabatt Name',
#                                     'class': 'form-control needs-validation',
#                                     'style': styling,
#                                     'name': 'discount_title',
#                                     'value': ''
#                                 }
#                             ))
#     discount = forms.DecimalField(required=True,
#                                   label='Rabatt',
#                                   widget=forms.NumberInput(
#                                       attrs={
#                                           'placeholder': 'Rabatt',
#                                           'class': 'form-control needs-validation',
#                                           'style': styling,
#                                           'name': 'discount_discount',
#                                           'value': ''
#                                       }
#                                   ))


# # Mitarbeiterverwaltung

# # Mitarbeiter
# class FormCreateEditEmployee(forms.Form):
#     firstname = forms.CharField(required=True,
#                                 label='Vorname',
#                                 widget=forms.TextInput(
#                                     attrs={
#                                         'placeholder': 'Vorname',
#                                         'class': 'form-control needs-validation',
#                                         'style': styling,
#                                         'name': 'employees_firstname',
#                                         'value': ''
#                                     }
#                                 ))
#     lastname = forms.CharField(required=True,
#                                label='Nachname',
#                                widget=forms.TextInput(
#                                    attrs={
#                                        'placeholder': 'Nachname',
#                                        'class': 'form-control needs-validation',
#                                        'style': styling,
#                                        'name': 'employees_lastname',
#                                        'value': ''
#                                    }
#                                ))
#     role = forms.CharField(required=True,
#                            label='Rolle',
#                            widget=forms.TextInput(
#                                attrs={
#                                    'placeholder': 'Rolle',
#                                    'class': 'form-control needs-validation',
#                                    'style': styling,
#                                    'name': 'employees_role',
#                                    'value': ''
#                                }
#                            ))
#     picture = forms.FileField(required=True,
#                               label='Bild',
#                               widget=forms.FileInput(
#                                   attrs={
#                                       'placeholder': 'Bild',
#                                       'class': 'form-control needs-validation',
#                                       'style': styling,
#                                       'name': 'employees_picture',
#                                       'value': ''
#                                   }
#                               ))


# # Systemverwaltung
# # Rechnungen
# class FromCreateEditInvoices(forms.Form):
#     id = forms.CharField(required=True,
#                          label='Rechnung-ID',
#                          widget=forms.TextInput(
#                              attrs={
#                                  'placeholder': 'Rechnung-ID',
#                                  'class': 'form-control needs-validation',
#                                  'style': styling,
#                                  'name': 'invoice_id',
#                                  'value': ''
#                              }
#                          ))


# # Kassen
# class FormCreateEditCashbox(forms.Form):
#     title = forms.CharField(required=True,
#                             label='Kasse-ID',
#                             widget=forms.TextInput(
#                                 attrs={
#                                     'placeholder': 'Kasse-ID',
#                                     'class': 'form-control needs-validation',
#                                     'style': styling,
#                                     'name': 'cashbox_id',
#                                     'value': ''
#                                 }
#                             ))
#     amount = forms.DecimalField(required=True,
#                                 label='Betrag',
#                                 widget=forms.NumberInput(
#                                     attrs={
#                                         'placeholder': 'Betrag',
#                                         'class': 'form-control needs-validation',
#                                         'style': styling,
#                                         'name': 'cashbox_amount',
#                                         'value': ''
#                                     }
#                                 ))


# # Safe
# class FormCreateEditSafe(forms.Form):
#     title = forms.CharField(required=True,
#                             label='Tresor-ID',
#                             widget=forms.TextInput(
#                                 attrs={
#                                     'placeholder': 'Tresor-ID',
#                                     'class': 'form-control needs-validation',
#                                     'style': styling,
#                                     'name': 'safe_id',
#                                     'value': ''
#                                 }
#                             ))
#     amount = forms.DecimalField(required=True,
#                                 label='Betrag',
#                                 widget=forms.NumberInput(
#                                     attrs={
#                                         'placeholder': 'Betrag',
#                                         'class': 'form-control needs-validation',
#                                         'style': styling,
#                                         'name': 'safe_amount',
#                                         'value': ''
#                                     }
#                                 ))


# # Kunden


# # Backup
# class FormCreateEditBackup(forms.Form):
#     title = forms.CharField(required=True,
#                             label='Backup Titel',
#                             widget=forms.TextInput(
#                                 attrs={
#                                     'placeholder': 'Backup Titel',
#                                     'class': 'form-control needs-validation',
#                                     'style': styling,
#                                     'name': 'backup_title',
#                                     'value': ''
#                                 }
#                             ))
#     creation = forms.DateTimeField(required=True,
#                                    label='Erstellt am',
#                                    widget=forms.DateInput(
#                                        attrs={
#                                            'placeholder': 'Erstellt am',
#                                            'class': 'form-control needs-validation',
#                                            'style': styling,
#                                            'name': 'backup_creation',
#                                            'value': ''
#                                        }
#                                    ))
#     store = forms.FileField(required=True,
#                             label='Pfad zur Backup-Datei',
#                             widget=forms.TextInput(
#                                 attrs={
#                                     'placeholder': 'Pfad zur Backup-Datei',
#                                     'class': 'form-control needs-validation',
#                                     'style': styling,
#                                     'name': 'backup_store',
#                                     'value': ''
#                                 }
#                             ))
#     comment = forms.CharField(required=True,
#                               label='Kommentar',
#                               widget=forms.TextInput(
#                                   attrs={
#                                       'placeholder': 'Kommentar',
#                                       'class': 'form-control needs-validation',
#                                       'style': styling,
#                                       'name': 'backup_comment',
#                                       'value': ''
#                                   }
#                               ))
#     employee = forms.CharField(required=True,
#                                label='Erstellt von',
#                                widget=forms.TextInput(
#                                    attrs={
#                                        'placeholder': 'Erstellt von',
#                                        'class': 'form-control needs-validation',
#                                        'style': styling,
#                                        'name': 'backup_employee',
#                                        'value': ''
#                                    }
#                                ))


# # Zahlungsmittel
# class FormCreateEditPayment(forms.Form):
#     title = forms.CharField(required=True,
#                             label='Zahlungsmittel',
#                             widget=forms.TextInput(
#                                 attrs={
#                                     'placeholder': 'Zahlungsmittel',
#                                     'class': 'form-control needs-validation',
#                                     'style': styling,
#                                     'name': 'payment_title',
#                                     'value': ''
#                                 }
#                             ))

#     picture = forms.FileField(required=True,
#                               label='Bild',
#                               widget=forms.FileInput(
#                                   attrs={
#                                       'placeholder': 'Bild',
#                                       'class': 'form-control needs-validation',
#                                       'style': styling,
#                                       'name': 'payment_picture',
#                                       'value': ''
#                                   }
#                               ))


# Anfragenverwaltung
#class FormRequest(forms.Form):
