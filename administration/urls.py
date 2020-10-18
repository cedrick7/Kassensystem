from django.urls import path


from .views import (
    productlist_view, 
    productdetail_view
)

app_name =  'administration'
urlpatterns=[
    path('Produkte', productlist_view, name='test_productlist'),
    path('Produkte/<int:id>', productdetail_view, name='test_productdetail'),
]

