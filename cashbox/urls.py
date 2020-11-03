from django.urls import path 
from authorization.decorators import allowed_user


from .views import (
    cashbox_dashboard_view,
    cashbox_payment_view,
    choose_cashbox_view,
    takeoutProduct,
    choose_paymenttool_view,

)


app_name =  'cashbox'
urlpatterns = [

    # Administration
    path('Auswählen', choose_cashbox_view.as_view(), name='cashbox_choose'),
    path('Kassieren', cashbox_dashboard_view.as_view(), name='cashbox_dashboard'),
    path('Zahlungsmittel', choose_paymenttool_view.as_view(), name='paymenttool_choose'),
    path('Payment', cashbox_payment_view.as_view(), name='cashbox_payment'),
    path('löschen', takeoutProduct, name='delete'),
    

    # path('', administration_dashboard, name='administration_dashboard'),

]