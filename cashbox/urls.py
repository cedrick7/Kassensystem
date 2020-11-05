from django.urls import path 
from authorization.decorators import allowed_user


from .views import (
    cashbox_dashboard_view,
    cashbox_payment_view,
    choose_cashbox_view,
    takeoutProduct,
    choose_paymenttool_view,
    cashbox_reversalbill_view,
    cashbox_customer_view,
    cashbox_customer_create_view,
    cashbox_customer_update_view,


)


app_name =  'cashbox'
urlpatterns = [

    # Administration
    path('Kasse', choose_cashbox_view.as_view(), name='cashbox_choose'),
    path('Warenkorb', cashbox_dashboard_view.as_view(), name='cashbox_dashboard'),
    path('Zahlungsmittel', choose_paymenttool_view.as_view(), name='paymenttool_choose'),
    path('Zahlung', cashbox_payment_view.as_view(), name='cashbox_payment'),
    path('löschen', takeoutProduct, name='delete'),
    path('Stornorechnung', cashbox_reversalbill_view.as_view(), name='cashbox_reversalbill'),
    path('Kundenkartei', cashbox_customer_view.as_view(), name='cashbox_customer'),
    path('Kundenkartei/Erstellen', cashbox_customer_create_view.as_view(), name='customer_create'),
    path('Kundenkartei/<int:id>/Bearbeiten', cashbox_customer_update_view.as_view(), name='customer_update'),
    
    

    # path('', administration_dashboard, name='administration_dashboard'),

]