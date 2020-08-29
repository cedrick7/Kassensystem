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

from auth.views import *
from costumer.views import *
from cashier.views import *
from admin.views import *
from analyst.views import *

urlpatterns = [
    path('', auth_login_view, name='login'),
    path('register/', auth_register_view, name='register'),
    path('forgot_password/', auth_forgot_password_view, name='forgot_password'),
    path('change_password/', auth_change_password_view, name='change_password'),

    path('costumer/', costumer_costumer_view, name='costumer'),

    path('kasse/', cashbox_dashboard_view, name='cashbox_dashboard'),
    path('kasse/pay/', cashbox_pay_view, name='pay'),
    path('kasse/more/', cashbox_more_view, name='more'),

    path('admin/', admin_dashboard_view, name='admin_dashboard'),
    path('admin/products/', admin_products_view, name='admin_products'),
    path('admin/products/detail/', admin_products_detail_view, name='admin_products_detail'),
    path('admin/services/', admin_services_view, name='admin_services'),
    path('admin/services/detail/', admin_services_detail_view, name='admin_services_detail'),
    path('admin/categories/', admin_categories_view, name='admin_categories'),
    path('admin/categories/detail/', admin_categories_detail_view, name='admin_categories_detail'),
    path('admin/attributes/', admin_attributes_view, name='admin_attributes'),
    path('admin/attributes/detail/', admin_attributes_detail_view, name='admin_attributes_detail'),
    path('admin/discounts/', admin_discounts_view, name='admin_discounts'),
    path('admin/discounts/detail/', admin_discounts_detail_view, name='admin_discounts_detail'),
    path('admin/employees/', admin_employees_view, name='admin_employees'),
    path('admin/employees/detail/', admin_employees_detail_view, name='admin_employees_detail'),
    path('admin/invoices/', admin_invoices_view, name='admin_invoices'),
    path('admin/invoices/detail/', admin_invoices_detail_view, name='admin_invoices_detail'),
    path('admin/cashboxes/', admin_cashboxes_view, name='admin_cashboxes'),
    path('admin/safes/', admin_safes_view, name='admin_safes'),
    path('admin/backups/', admin_backups_view, name='admin_backups'),
    path('admin/backups/detail/', admin_backups_detail_view, name='admin_backups_detail'),
    path('admin/payments/', admin_payments_view, name='admin_payments'),
    path('admin/requests/', admin_requests_view, name='admin_requests'),

    path('analyst/', analyst_dashboard_view, name='analyst_dashboard'),
    path('analyst/sales/', analyst_sales_view, name='analyst_sales'),
    path('analyst/costumers/', analyst_costumers_view, name='analyst_costumers'),
    path('analyst/employees/', analyst_employees_view, name='analyst_employees'),

    path('superuser/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
