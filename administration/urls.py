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
    

)

app_name =  'administration'
urlpatterns=[
    
    # Administration
    path('', administration_dashboard, name='administration_dashboard'),

    # Produkte
    path('Produkte', ProductListView.as_view(), name='product_list'),
    path('Produkte/Erstellen', ProductCreateView.as_view(), name='product_create'),
    path('Produkte/<int:id>/Bearbeiten', ProductUpdateView.as_view(), name='product_update'),
    path('Produkte/<int:id>/Delete', ProductDeleteView.as_view(), name='product_delete'),

    # Kategorien
    path('Kategorien', CategoryListView.as_view(), name='category_list'),
    path('Kategorien/Erstellen', CategoryCreateView.as_view(), name='category_create'),
    path('Kategorien/<int:id>/Bearbeiten', CategoryUpdateView.as_view(), name='category_update'),
    path('Kategorien/<int:id>/Delete', CategoryDeleteView.as_view(), name='category_delete'),

    # Rabatt
    path('Rabatte', DiscountListView.as_view(), name='discount_list'),
    path('Rabatte/Erstellen', DiscountCreateView.as_view(), name='discount_create'),
    path('Rabatte/<int:id>/Bearbeiten', DiscountUpdateView.as_view(), name='discount_update'),
    path('Rabatte/<int:id>/Delete', DiscountDeleteView.as_view(), name='discount_delete'),




]

