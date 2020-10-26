from django.urls import path 
from authorization.decorators import allowed_user


from .views import (
    administration_dashboard,
   
    ProductListView,  
    ProductCreateView, 
    ProductUpdateView, 
    ProductDeleteView, 

    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView, 
    CategoryDeleteView,

    DiscountListView,
    DiscountCreateView,
    DiscountUpdateView,
    DiscountDeleteView,
    
    TaxListView,
    TaxCreateView,
    TaxUpdateView,
    TaxDeleteView,

    AttributeListView,
    AttributeCreateView,
    AttributeUpdateView,
    AttributeDeleteView,

    CustomerListView,
    CustomerCreateView,
    CustomerUpdateView,
    CustomerDeleteView,

    EmployeeListView,
    EmployeeUpdateView,
    EmployeeDeleteView,

    WorkTimeListView,

    SafeListView,
    SafeCreateView,
    SafeUpdateView,
    SafeDeleteView,

    CashboxListView,
    CashboxCreateView, 
    CashboxUpdateView, 
    CashboxDeleteView,


    PaymenttoolListView,
    PaymenttoolCreateView,
    PaymenttoolUpdateView,
    PaymenttoolDeleteView,

    BackupListView,
    BackupCreateView,
    BackupUpdateView,
    BackupDeleteView,

    BillListView, 
    BillDetailView,
    BillCreateView,

    ReversalBillListView,
    ReversalBillDetailView,
    ReversalBillCreateView,

)

app_name =  'administration'
urlpatterns=[

    # Administration
    path('', administration_dashboard, name='administration_dashboard'),

    # Produkte
    path('Produkte', allowed_user(allowed_roles=['Administratoren'])(ProductListView.as_view()), name='product_list'),
    path('Produkte/Erstellen', allowed_user(allowed_roles=['Administratoren'])(ProductCreateView.as_view()), name='product_create'),
    path('Produkte/<int:id>/Bearbeiten', allowed_user(allowed_roles=['Administratoren'])(ProductUpdateView.as_view()), name='product_update'),
    path('Produkte/<int:id>/Löschen', allowed_user(allowed_roles=['Administratoren'])(ProductDeleteView.as_view()), name='product_delete'),

    # Kategorien
    path('Kategorien', allowed_user(allowed_roles=['Administratoren'])(CategoryListView.as_view()), name='category_list'),
    path('Kategorien/Erstellen', allowed_user(allowed_roles=['Administratoren'])(CategoryCreateView.as_view()), name='category_create'),
    path('Kategorien/<int:id>/Bearbeiten', allowed_user(allowed_roles=['Administratoren'])(CategoryUpdateView.as_view()), name='category_update'),
    path('Kategorien/<int:id>/Löschen', allowed_user(allowed_roles=['Administratoren'])(CategoryDeleteView.as_view()), name='category_delete'),

    # Rabatt
    path('Rabatte', allowed_user(allowed_roles=['Administratoren'])(DiscountListView.as_view()), name='discount_list'),
    path('Rabatte/Erstellen', allowed_user(allowed_roles=['Administratoren'])(DiscountCreateView.as_view()), name='discount_create'),
    path('Rabatte/<int:id>/Bearbeiten', allowed_user(allowed_roles=['Administratoren'])(DiscountUpdateView.as_view()), name='discount_update'),
    path('Rabatte/<int:id>/Löschen', allowed_user(allowed_roles=['Administratoren'])(DiscountDeleteView.as_view()), name='discount_delete'),

    # Steuersätze
    path('Steuersätze', allowed_user(allowed_roles=['Administratoren'])(TaxListView.as_view()), name='tax_list'),
    path('Steuersätze/Erstellen', allowed_user(allowed_roles=['Administratoren'])(TaxCreateView.as_view()), name='tax_create'),
    path('Steuersätze/<int:id>/Bearbeiten', allowed_user(allowed_roles=['Administratoren'])(TaxUpdateView.as_view()), name='tax_update'),
    path('Steuersätze/<int:id>/Löschen', allowed_user(allowed_roles=['Administratoren'])(TaxDeleteView.as_view()), name='tax_delete'),

    # Attribute
    path('Attribute', allowed_user(allowed_roles=['Administratoren'])(AttributeListView.as_view()), name='attribute_list'),
    path('Attribute/Erstellen', allowed_user(allowed_roles=['Administratoren'])(AttributeCreateView.as_view()), name='attribute_create'),
    path('Attribute/<int:id>/Bearbeiten', allowed_user(allowed_roles=['Administratoren'])(AttributeUpdateView.as_view()), name='attribute_update'),
    path('Attribute/<int:id>/Löschen', allowed_user(allowed_roles=['Administratoren'])(AttributeDeleteView.as_view()), name='attribute_delete'),

    # Kunden
    path('Kunden', allowed_user(allowed_roles=['Administratoren'])(CustomerListView.as_view()), name='customer_list'),
    path('Kunden/Erstellen', allowed_user(allowed_roles=['Administratoren'])(CustomerCreateView.as_view()), name='customer_create'),
    path('Kunden/<int:id>/Bearbeiten', allowed_user(allowed_roles=['Administratoren'])(CustomerUpdateView.as_view()), name='customer_update'),
    path('Kunden/<int:id>/Löschen', allowed_user(allowed_roles=['Administratoren'])(CustomerDeleteView.as_view()), name='customer_delete'),

    # Mitarbeiter
    path('Mitarbeiter', allowed_user(allowed_roles=['Administratoren'])(EmployeeListView.as_view()), name='employee_list'),
    path('Mitarbeiter/<int:id>/Bearbeiten', allowed_user(allowed_roles=['Administratoren'])(EmployeeUpdateView.as_view()), name='employee_update'),
    path('Mitarbeiter/<int:id>/Löschen', allowed_user(allowed_roles=['Administratoren'])(EmployeeDeleteView.as_view()), name='employee_delete'),

    # Arbeitszeiten
    path('Arbeitszeiten', allowed_user(allowed_roles=['Administratoren'])(WorkTimeListView.as_view()), name='worktime_list'),

    # Safes
    path('Safes', allowed_user(allowed_roles=['Administratoren'])(SafeListView.as_view()), name='safe_list'),
    path('Safes/Erstellen', allowed_user(allowed_roles=['Administratoren'])(SafeCreateView.as_view()), name='safe_create'),
    path('Safes/<int:id>/Bearbeiten', allowed_user(allowed_roles=['Administratoren'])(SafeUpdateView.as_view()), name='safe_update'),
    path('Safes/<int:id>/Löschen', allowed_user(allowed_roles=['Administratoren'])(SafeDeleteView.as_view()), name='safe_delete'),

    # Kassen
    path('Kassen', allowed_user(allowed_roles=['Administratoren'])(CashboxListView.as_view()), name='cashbox_list'),
    path('Kassen/Erstellen', allowed_user(allowed_roles=['Administratoren'])(CashboxCreateView.as_view()), name='cashbox_create'),
    path('Kassen/<int:id>/Bearbeiten', allowed_user(allowed_roles=['Administratoren'])(CashboxUpdateView.as_view()), name='cashbox_update'),
    path('Kassen/<int:id>/Löschen', allowed_user(allowed_roles=['Administratoren'])(CashboxDeleteView.as_view()), name='cashbox_delete'),


    # Zahlungsmittel
    path('Zahlungsmittel', allowed_user(allowed_roles=['Administratoren'])(PaymenttoolListView.as_view()), name='paymenttool_list'),
    path('Zahlungsmittel/Erstellen', allowed_user(allowed_roles=['Administratoren'])(PaymenttoolCreateView.as_view()), name='paymenttool_create'),
    path('Zahlungsmittel/<int:id>/Bearbeiten', allowed_user(allowed_roles=['Administratoren'])(PaymenttoolUpdateView.as_view()), name='paymenttool_update'),
    path('Zahlungsmittel/<int:id>/Löschen', allowed_user(allowed_roles=['Administratoren'])(PaymenttoolDeleteView.as_view()), name='paymenttool_delete'),


    # Datensicherungen
    path('Datensicherungen', allowed_user(allowed_roles=['Administratoren'])(BackupListView.as_view()), name='backup_list'),
    path('Datensicherungen/Erstellen', allowed_user(allowed_roles=['Administratoren'])(BackupCreateView.as_view()), name='backup_create'),
    path('Datensicherungen/<int:id>/Bearbeiten', allowed_user(allowed_roles=['Administratoren'])(BackupUpdateView.as_view()), name='backup_update'),
    path('Datensicherungen/<int:id>/Löschen', allowed_user(allowed_roles=['Administratoren'])(BackupDeleteView.as_view()), name='backup_delete'),

    # Rechnungen
    path('Rechnungen', allowed_user(allowed_roles=['Administratoren'])(BillListView.as_view()), name='bill_list'),
    path('Rechnungen/<int:id>/Details', allowed_user(allowed_roles=['Administratoren'])(BillDetailView.as_view()), name='bill_details'),
    path('Rechnungen/Erstellen', allowed_user(allowed_roles=['Administratoren'])(BillCreateView.as_view()), name='bill_create'), # muss noch raus, dient nur zu Testzwecken, nicht stylen

    # Rechnungen
    path('Stornorechnungen', allowed_user(allowed_roles=['Administratoren'])(ReversalBillListView.as_view()), name='reversalbill_list'),
    path('Stornorechnungen/<int:id>/Details', allowed_user(allowed_roles=['Administratoren'])(ReversalBillDetailView.as_view()), name='reversalbill_details'),
    path('Stornorechnungen/Erstellen', allowed_user(allowed_roles=['Administratoren'])(ReversalBillCreateView.as_view()), name='reversalbill_create'), # muss noch raus, dient nur zu Testzwecken, nicht stylen
    



]

