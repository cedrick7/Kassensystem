"""Kassensystem URL Configuration

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
from django.urls import path, include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from authorization.views import *
from customer.views import *
from cashbox.views import *
from administration.views import *
from analyzation.views import *
from administration.urls import * 
from cashbox.urls import *
from django.urls import include, path

urlpatterns = [

    path('Administration/', include('administration.urls')),
    path('Autorisierung/', include('authorization.urls')),
    path('Kasse/', include('cashbox.urls')),


    path('Kunden/', customer_customer_view, name='customer'),

    # path('Kasse/', cashbox_dashboard_view, name='cashbox_dashboard'),
    # path('Kasse/Bezahlen/', cashbox_pay_view, name='cashbox_pay'),
    # path('Kasse/Mehr/', cashbox_more_view, name='cashbox_more'),

    # path('Admin/', administration_dashboard_view, name='administration_dashboard'),
    # path('Admin/Produkte/', administration_products_view, name='administration_products'),
    # path('Admin/Produkte/Details/<int:id>/', administration_products_detail_view, name='administration_products_detail'),
    # path('Admin/Dienstleistungen/', administration_services_view, name='administration_services'),
    # path('Admin/Dienstleistungen/Details/', administration_services_detail_view, name='administration_services_detail'),
    # path('Admin/Kategorien/', administration_categories_view, name='administration_categories'),
    # path('Admin/Kategorien/Details/', administration_categories_detail_view, name='administration_categories_detail'),
    # path('Admin/Eigenschaften/', administration_attributes_view, name='administration_attributes'),
    # path('Admin/Eigenschaften/Details/', administration_attributes_detail_view, name='administration_attributes_detail'),
    # path('Admin/Rabatte/', administration_discounts_view, name='administration_discounts'),
    # path('Admin/Rabatte/Details/', administration_discounts_detail_view, name='administration_discounts_detail'),
    # path('Admin/Mitarbeiter/', administration_employees_view, name='administration_employees'),
    # path('Admin/Mitarbeiter/Details/', administration_employees_detail_view, name='administration_employees_detail'),
    # path('Admin/Rechnungen/', administration_invoices_view, name='administration_invoices'),
    # path('Admin/Rechnungen/Details/', administration_invoices_detail_view, name='administration_invoices_detail'),
    # path('Admin/Kassen/', administration_cashboxes_view, name='administration_cashboxes'),
    # path('Admin/Tresore/', administration_safes_view, name='administration_safes'),
    # path('Admin/Backups/', administration_backups_view, name='administration_backups'),
    # path('Admin/Backups/Details/', administration_backups_detail_view, name='administration_backups_detail'),
    # path('Admin/Zahlungsmittel/', administration_payments_view, name='administration_payments'),
    # path('Admin/Anfragen/', administration_requests_view, name='administration_requests'),

    path('Analyst/', analyzation_dashboard_view, name='analyzation_dashboard'),
    path('Analyst/Umsatz/', analyzation_sales_view, name='analyzation_sales'),
    path('Analyst/Kunden/', analyzation_customers_view, name='analyzation_customers'),
    path('Analyst/Mitarbeiter/', analyzation_employees_view, name='analyzation_employees'),

    path('superuser/', admin.site.urls),

    #url(r'^Analyst/$', DashboardView.as_view(), name='analyzation_dashboard'),
    #url(r'^api/data/$', get_data, name='api-data'),
    url(r'^api/dashboard/chart/data/$', DashboardChartData.as_view(), name='api-dashboard-chart-data'),
    url(r'^api/sales/chart/data/$', SalesChartData.as_view(), name='api-sales-chart-data'),
    url(r'^api/customers/chart/data/$', CustomerChartData.as_view(), name='api-customers-chart-data'),
    url(r'^api/employees/chart/data/$', EmployeeChartData.as_view(), name='api-employees-chart-data'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
