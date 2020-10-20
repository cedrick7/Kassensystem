from django.urls import path


from .views import (
    ProductListView, 
    # ProductDetailView, 
    ProductCreateView, 
    ProductUpdateView, 
    ProductDeleteView, 
    administration_dashboard,

)

app_name =  'administration'
urlpatterns=[
    
    path('', administration_dashboard, name='administration_dashboard'),
    path('Produkte', ProductListView.as_view(), name='product_list'),
    # path('Produkte/<int:id>', ProductDetailView.as_view(), name='test_productdetail'),
    path('Produkte/Erstellen', ProductCreateView.as_view(), name='product_create'),
    path('Produkte/<int:id>/Bearbeiten', ProductUpdateView.as_view(), name='product_update'),
    path('Produkte/<int:id>/Delete', ProductDeleteView.as_view(), name='product_delete'),





]

