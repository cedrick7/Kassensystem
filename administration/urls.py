from django.urls import path


from .views import (
    ProductListView, 
    ProductDetailView, 
    ProductCreateView, 
    ProductUpdateView
)

app_name =  'administration'
urlpatterns=[
    path('Produkte', ProductListView.as_view(), name='test_productlist'),
    path('Produkte/<int:id>', ProductDetailView.as_view(), name='test_productdetail'),
    path('Produkte/Erstellen', ProductCreateView.as_view(), name='test_productcreate'),
    path('Produkte/<int:id>/Bearbeiten', ProductUpdateView.as_view(), name='test_productupdate'),
]

