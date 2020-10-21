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

    #Attribute
    path('Attribute', AttributeListView.as_view(), name='attribute_list'),
    path('Attribute/Erstellen', AttributeCreateView.as_view(), name='attribute_create'),
    path('Attribute/<int:id>/Bearbeiten', AttributeUpdateView.as_view(), name='attribute_update'),
    path('Attribute/<int:id>/Löschen', AttributeDeleteView.as_view(), name='attribute_delete'),


]

