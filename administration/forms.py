from django import forms
from .models import *
from authorization.models import *
from analyzation.models import *
from cashbox.models import *
from customer.models import *
from product.models import *
from authorization.models import *
from django.contrib.auth.models import User

styling = ''

choices = (
    ('cashier', 'Kassierer'),
    ('admin', 'Administrator'),
    ('analyst', 'Analyst')
)


class AttributeModelForm(forms.ModelForm):
    class Meta:
        model = Attribute
        fields = [
            'title',
        ]
        widgets = {

            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Titel',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'attribute_title',
                    'value': '',
                }
            )

        }


class BackupModelForm(forms.ModelForm):
    class Meta:
        model = Backup
        fields = [
            'title',
            'comment',
            'creation',
            'employee',
        ]
        widgets = {

            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Backupname',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'backup_title',
                    'value': '',
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'placeholder': 'Kommentar',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'backup_comment',
                    'value': '',
                }
            ),
            'creation': forms.DateTimeInput(
                attrs={
                    'placeholder': 'Erstellungsdatum',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'backup_employee',
                    'value': '',
                }

            ),
            'employee': forms.TextInput(
                attrs={
                    'placeholder': 'Ersteller',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'backup_employee',
                    'value': '',
                }
            )

        }


class CashboxModelForm(forms.ModelForm):
    class Meta:
        model = Cashbox
        fields = [
            'title',
            'amount'
        ]
        widgets = {

            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Kasse',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'cashbox_title',
                    'value': '',
                }
            ),
            'amount': forms.NumberInput(
                attrs={
                    'placeholder': 'Geldinhalt',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'cashbox_amount',
                    'value': '1000.00',
                }
            ),
        }


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'title',
            'color',
            'discount',
        ]

        widgets = {

            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Kasse',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'category_title',
                    'value': '',
                }
            ),
            'color': forms.TextInput(
                attrs={
                    'placeholder': 'Farbe',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'category_color',
                    'value': '',
                }
            ),
            'discount': forms.NumberInput(
                attrs={
                    'placeholder': 'Rabatt',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'category_discount',
                    'value': '',
                }
            ),
        }


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
        widgets = {

            'firstname': forms.TextInput(
                attrs={
                    'placeholder': 'Vorname',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'customer_firstname',
                    'value': '',
                }
            ),

            'lastname': forms.TextInput(
                attrs={
                    'placeholder': 'Nachname',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'customer_lastname',
                    'value': '',
                }
            ),
            'birthday': forms.DateInput(
                attrs={
                    'placeholder': 'geburtstag',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'customer_firstname',
                    'value': '01.01.1999',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'customer_firstname',
                    'value': '',
                }
            ),
            'phonenumber': forms.NumberInput(
                attrs={
                    'placeholder': 'Mobil-Nummer',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'customer_phonenumber',
                    'value': '',
                }
            ),
        }


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

        widgets = {

            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Name',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'discount_title',
                    'value': '',
                }
            ),

            'factor': forms.NumberInput(
                attrs={
                    'placeholder': 'Faktor',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'discount_factor',
                    'value': '',
                }
            ),
            'amount': forms.NumberInput(
                attrs={
                    'placeholder': 'Rabattsatz',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'discount_amount',
                    'value': '',
                }
            ),
            'begin': forms.DateInput(
                attrs={
                    'placeholder': 'Beginn',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'discount_begin',
                    'value': '',
                }
            ),
            'end': forms.DateInput(
                attrs={
                    'placeholder': 'Ende',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'discount_end',
                    'value': '',
                }
            ),
        }


class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password',
            'date_joined',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
            'groups',
        ]


#        widgets = {
#            'firstname': forms.TextInput(
#                attrs={
#                    'placeholder': 'Vorname',
#                    'class': 'form-control needs-validation',
#                    'style': styling,
#                    'name': 'employee_firstname',
#                    'value': ''
#                }
#            ),
#
#            'lastname': forms.TextInput(
#                attrs={
#                    'placeholder': 'Nachname',
#                    'class': 'form-control needs-validation',
#                    'style': styling,
#                    'name': 'employee_lastname',
#                    'value': ''
#                }
#            ),
#
#            'password': forms.PasswordInput(
#                attrs={
#                    'placeholder': 'Passwort',
#                    'class': 'form-control needs-validation',
#                    'style': styling,
#                    'name': 'employee_password',
#                    'value': ''
#                }
#            ),
#
#            'picture': forms.FileInput(
#                attrs={
#                    'placeholder': '',
#                    'class': 'form-control needs-validation',
#                    'style': styling,
#                    'name': 'employee_picture',
#                    'value': ''
#                }
#            ),
#
#            'role': forms.ModelChoiceField(
#                attrs={
#                    'placeholder': '',
#                    'class': 'form-control needs-validation',
#                    'style': styling,
#                    'name': 'employee_role',
#                    'value': ''
#                }
#            ),
#        }

class PaymenttoolModelForm(forms.ModelForm):
    class Meta:
        model = Paymenttool
        fields = [
            'title',
            'path',
        ]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Zahlungstyp',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'paymenttool_title',
                    'value': ''
                }
            ),

            'path': forms.Textarea(
                attrs={
                    'placeholder': 'Pfad',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'paymenttool_path',
                    'value': ''
                }
            ),
        }


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
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Produkttyp',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'product_type',
                    'value': ''
                }
            ),
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Produktname',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'product_title',
                    'value': '',
                }
            ),
            'category': forms.TextInput(
                attrs={
                    'placeholder': 'Kategorie',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'product_category',
                    'value': ''
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Beschreibung',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'product_description',
                    'value': ''
                }
            ),
            'cost': forms.NumberInput(
                attrs={
                    'placeholder': 'Preis',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'product_cost',
                    'value': ''
                }
            ),
            'weight': forms.NumberInput(
                attrs={
                    'placeholder': 'gewicht',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'product_weight',
                    'value': ''
                }
            ),
            'stock': forms.NumberInput(
                attrs={
                    'placeholder': 'Anzahl',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'product_stock',
                    'value': ''
                }
            ),
            'brand': forms.TextInput(
                attrs={
                    'placeholder': 'Marke',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'product_brand',
                    'value': ''
                }
            ),
            'tax': forms.NumberInput(
                attrs={
                    'placeholder': 'MW-Steuer',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'product_tax',
                    'value': ''
                }
            ),
            'discount': forms.NumberInput(
                attrs={
                    'placeholder': 'Rabatt',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'product_discount',
                    'value': ''
                }
            ),
            'path': forms.Textarea(
                attrs={
                    'placeholder': 'Pfad',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'product_path',
                    'value': ''
                }
            ),
            'attributes': forms.Textarea(
                attrs={
                    'placeholder': 'Attribute',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'product_attributes',
                    'value': ''
                }
            ),
        }


class SafeModelForm(forms.ModelForm):
    class Meta:
        model = Safe
        fields = [
            'title',
            'amount'
        ]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Name',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'safe_title',
                    'value': ''
                }
            ),
            'amount': forms.NumberInput(
                attrs={
                    'placeholder': 'Geldstand',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'safe_amount',
                    'value': '1000.00'
                }
            ),

        }


class TaxModelForm(forms.ModelForm):
    class Meta:
        model = Tax
        fields = [
            'title',
            'taxrate',
        ]
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Name',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'tax_title',
                    'value': ''
                }
            ),
            'taxrate': forms.NumberInput(
                attrs={
                    'placeholder': 'Mw-Steuer',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'tax_taxrate',
                    'value': ''
                }
            ),
        }


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
        widgets = {
            'creation': forms.DateTimeInput(
                attrs={
                    'placeholder': 'Erstelldatum',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'bill_creation',
                    'value': ''
                }
            ),
            'totalcosts': forms.NumberInput(
                attrs={
                    'placeholder': 'Gesammtkosten',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'bill_totalcosts',
                    'value': ''
                }
            ),
            'employee': forms.TextInput(
                attrs={
                    'placeholder': 'Mitarbeiter',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'bill_employee',
                    'value': ''
                }
            ),
            'cashbox': forms.TextInput(
                attrs={
                    'placeholder': 'Kassenname',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'bill_cashbox',
                    'value': ''
                }
            ),
            'paymenttool': forms.TextInput(
                attrs={
                    'placeholder': 'Zahlungsart',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'bill_paymenttool',
                    'value': ''
                }
            ),
            'discount': forms.NumberInput(
                attrs={
                    'placeholder': 'Rabatt',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'bill_discount',
                    'value': ''
                }
            ),
            'path': forms.Textarea(
                attrs={
                    'placeholder': 'Pfad',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'bill_path',
                    'value': ''
                }
            ),
        }


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

        widgets = {
            'bill': forms.TextInput(
                attrs={
                    'placeholder': 'Name',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'reversalbill_bill',
                    'value': ''
                }
            ),

            'creation': forms.DateTimeInput(
                attrs={
                    'placeholder': 'Erstellt am',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'reversalbill_creation',
                    'value': ''
                }
            ),

            'refund': forms.NumberInput(
                attrs={
                    'placeholder': 'Erstattung',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'reversalbill_refund',
                    'value': ''
                }
            ),

            'employee': forms.TextInput(
                attrs={
                    'placeholder': 'Mitarbeiter',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'reversalbill_employee',
                    'value': ''
                }
            ),

            'cashbox': forms.TextInput(
                attrs={
                    'placeholder': 'Kasse',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'reversalbill_cashbox',
                    'value': ''
                }
            ),

            'path': forms.Textarea(
                attrs={
                    'placeholder': 'Pfad',
                    'class': 'form-control needs-validation',
                    'style': styling,
                    'name': 'reversalbill_path',
                    'value': ''
                }
            ),
        }


class WorkTimeModelForm(forms.ModelForm):
    class Meta:
        model = Worktime
        fields = [
            'employee',
            'begin',
            'end',
        ]

    widgets = {
        'employee': forms.TextInput(
            attrs={
                'placeholder': 'mitarbeiter',
                'class': 'form-control needs-validation',
                'style': styling,
                'name': 'worktime_employee',
                'value': ''
            }
        ),

        'begin': forms.TextInput(
            attrs={
                'placeholder': 'Eingecheckt',
                'class': 'form-control needs-validation',
                'style': styling,
                'name': 'worktime_begin',
                'value': ''
            }
        ),

        'end': forms.TextInput(
            attrs={
                'placeholder': 'Ausgecheckt',
                'class': 'form-control needs-validation',
                'style': styling,
                'name': 'worktime_end',
                'value': ''
            }
        ),
    }


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
