from django.urls import include, path


from .views import (
    productlist_view, 
    productdetail_view
)

app_name =  'administration'
urlpatterns=[
    path('pl', productlist_view, name='test_productlist'),
    path('pl/<int:id>', productdetail_view, name='test_productdetail'),
]

