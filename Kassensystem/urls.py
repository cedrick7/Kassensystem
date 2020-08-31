"""Projekt1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from authorization.views import *
from costumer.views import *
from cashbox.views import *
from administration.views import *
from analyzation.views import *

urlpatterns = [
    path('', authorization_login_view, name='authorization_login'),
    path('register/', authorization_register_view, name='authorization_register'),
    path('forgot_password/', authorization_forgot_password_view, name='authorization_forgot_password'),
    path('change_password/', authorization_change_password_view, name='authorization_change_password'),

    path('costumer/', costumer_costumer_view, name='costumer'),

    path('kasse/', cashbox_dashboard_view, name='cashbox_dashboard'),
    path('kasse/pay/', cashbox_pay_view, name='cashbox_pay'),
    path('kasse/more/', cashbox_more_view, name='cashbox_more'),

    path('administration/', administration_dashboard_view, name='administration_dashboard'),
    path('administration/products/', administration_products_view, name='administration_products'),
    path('administration/products/detail/', administration_products_detail_view, name='administration_products_detail'),
    path('administration/services/', administration_services_view, name='administration_services'),
    path('administration/services/detail/', administration_services_detail_view, name='administration_services_detail'),
    path('administration/categories/', administration_categories_view, name='administration_categories'),
    path('administration/categories/detail/', administration_categories_detail_view, name='administration_categories_detail'),
    path('administration/attributes/', administration_attributes_view, name='administration_attributes'),
    path('administration/attributes/detail/', administration_attributes_detail_view, name='administration_attributes_detail'),
    path('administration/discounts/', administration_discounts_view, name='administration_discounts'),
    path('administration/discounts/detail/', administration_discounts_detail_view, name='administration_discounts_detail'),
    path('administration/employees/', administration_employees_view, name='administration_employees'),
    path('administration/employees/detail/', administration_employees_detail_view, name='administration_employees_detail'),
    path('administration/invoices/', administration_invoices_view, name='administration_invoices'),
    path('administration/invoices/detail/', administration_invoices_detail_view, name='administration_invoices_detail'),
    path('administration/cashboxes/', administration_cashboxes_view, name='administration_cashboxes'),
    path('administration/safes/', administration_safes_view, name='administration_safes'),
    path('administration/backups/', administration_backups_view, name='administration_backups'),
    path('administration/backups/detail/', administration_backups_detail_view, name='administration_backups_detail'),
    path('administration/payments/', administration_payments_view, name='administration_payments'),
    path('administration/requests/', administration_requests_view, name='administration_requests'),

    path('analyzation/', analyzation_dashboard_view, name='analyzation_dashboard'),
    path('analyzation/sales/', analyzation_sales_view, name='analyzation_sales'),
    path('analyzation/costumers/', analyzation_costumers_view, name='analyzation_costumers'),
    path('analyzation/employees/', analyzation_employees_view, name='analyzation_employees'),

    path('superuser/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
