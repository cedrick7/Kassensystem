from django.urls import path


from .views import (
    ProductListView,  
    ProductCreateView, 
    ProductUpdateView, 
    ProductDeleteView, 
    administration_dashboard,
    CategoryListView,
    CategoryCreateView,
    CategoryUpdateView, 
    CategoryDeleteView,
    

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





]

