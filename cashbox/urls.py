from django.urls import path 
from authorization.decorators import allowed_user


from .views import (
    cashbox_dashboard_view,
)


app_name =  'cashbox'
urlpatterns = [

    # Administration
    path('', cashbox_dashboard_view.as_view(), name='cashbox_dashboard'),
    # path('', administration_dashboard, name='administration_dashboard'),
    # path('', administration_dashboard, name='administration_dashboard'),

]