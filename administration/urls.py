from django.urls import path


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
    path('Produkte', ProductListView.as_view(), name='product_list'),
    path('Produkte/Erstellen', ProductCreateView.as_view(), name='product_create'),
    path('Produkte/<int:id>/Bearbeiten', ProductUpdateView.as_view(), name='product_update'),
    path('Produkte/<int:id>/Löschen', ProductDeleteView.as_view(), name='product_delete'),

    # Kategorien
    path('Kategorien', CategoryListView.as_view(), name='category_list'),
    path('Kategorien/Erstellen', CategoryCreateView.as_view(), name='category_create'),
    path('Kategorien/<int:id>/Bearbeiten', CategoryUpdateView.as_view(), name='category_update'),
    path('Kategorien/<int:id>/Löschen', CategoryDeleteView.as_view(), name='category_delete'),

    # Rabatt
    path('Rabatte', DiscountListView.as_view(), name='discount_list'),
    path('Rabatte/Erstellen', DiscountCreateView.as_view(), name='discount_create'),
    path('Rabatte/<int:id>/Bearbeiten', DiscountUpdateView.as_view(), name='discount_update'),
    path('Rabatte/<int:id>/Löschen', DiscountDeleteView.as_view(), name='discount_delete'),

    # Steuersätze
    path('Steuersätze', TaxListView.as_view(), name='tax_list'),
    path('Steuersätze/Erstellen', TaxCreateView.as_view(), name='tax_create'),
    path('Steuersätze/<int:id>/Bearbeiten', TaxUpdateView.as_view(), name='tax_update'),
    path('Steuersätze/<int:id>/Löschen', TaxDeleteView.as_view(), name='tax_delete'),

    # Attribute
    path('Attribute', AttributeListView.as_view(), name='attribute_list'),
    path('Attribute/Erstellen', AttributeCreateView.as_view(), name='attribute_create'),
    path('Attribute/<int:id>/Bearbeiten', AttributeUpdateView.as_view(), name='attribute_update'),
    path('Attribute/<int:id>/Löschen', AttributeDeleteView.as_view(), name='attribute_delete'),

    # Kunden
    path('Kunden', CustomerListView.as_view(), name='customer_list'),
    path('Kunden/Erstellen', CustomerCreateView.as_view(), name='customer_create'),
    path('Kunden/<int:id>/Bearbeiten', CustomerUpdateView.as_view(), name='customer_update'),
    path('Kunden/<int:id>/Löschen', CustomerDeleteView.as_view(), name='customer_delete'),

    # Mitarbeiter
    path('Mitarbeiter', EmployeeListView.as_view(), name='employee_list'),
    path('Mitarbeiter/<int:id>/Bearbeiten', EmployeeUpdateView.as_view(), name='employee_update'),
    path('Mitarbeiter/<int:id>/Löschen', EmployeeDeleteView.as_view(), name='employee_delete'),

    # Arbeitszeiten
    path('Arbeitszeiten', WorkTimeListView.as_view(), name='worktime_list'),

    # Safes
    path('Safes', SafeListView.as_view(), name='safe_list'),
    path('Safes/Erstellen', SafeCreateView.as_view(), name='safe_create'),
    path('Safes/<int:id>/Bearbeiten', SafeUpdateView.as_view(), name='safe_update'),
    path('Safes/<int:id>/Löschen', SafeDeleteView.as_view(), name='safe_delete'),

    # Kassen
    path('Kassen', CashboxListView.as_view(), name='cashbox_list'),
    path('Kassen/Erstellen', CashboxCreateView.as_view(), name='cashbox_create'),
    path('Kassen/<int:id>/Bearbeiten', CashboxUpdateView.as_view(), name='cashbox_update'),
    path('Kassen/<int:id>/Löschen', CashboxDeleteView.as_view(), name='cashbox_delete'),


    # Zahlungsmittel
    path('Zahlungsmittel', PaymenttoolListView.as_view(), name='paymenttool_list'),
    path('Zahlungsmittel/Erstellen', PaymenttoolCreateView.as_view(), name='paymenttool_create'),
    path('Zahlungsmittel/<int:id>/Bearbeiten', PaymenttoolUpdateView.as_view(), name='paymenttool_update'),
    path('Zahlungsmittel/<int:id>/Löschen', PaymenttoolDeleteView.as_view(), name='paymenttool_delete'),


    # Datensicherungen
    path('Datensicherungen', BackupListView.as_view(), name='backup_list'),
    path('Datensicherungen/Erstellen', BackupCreateView.as_view(), name='backup_create'),
    path('Datensicherungen/<int:id>/Bearbeiten', BackupUpdateView.as_view(), name='backup_update'),
    path('Datensicherungen/<int:id>/Löschen', BackupDeleteView.as_view(), name='backup_delete'),

    # Rechnungen
    path('Rechnungen', BillListView.as_view(), name='bill_list'),
    path('Rechnungen/<int:id>/Details', BillDetailView.as_view(), name='bill_details'),
    path('Rechnungen/Erstellen', BillCreateView.as_view(), name='bill_create'), # muss noch raus, dient nur zu Testzwecken, nicht stylen

    # Rechnungen
    path('Stornorechnungen', ReversalBillListView.as_view(), name='reversalbill_list'),
    path('Stornorechnungen/<int:id>/Details', ReversalBillDetailView.as_view(), name='reversalbill_details'),
    path('Stornorechnungen/Erstellen', ReversalBillCreateView.as_view(), name='reversalbill_create'), # muss noch raus, dient nur zu Testzwecken, nicht stylen
    



]

