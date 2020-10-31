from django.urls import path
from authorization.decorators import allowed_user
from .views import *
from django.conf.urls import url


app_name =  'analyzation'

urlpatterns=[
    path('', analyzation_dashboard_view, name='analyzation_dashboard'),
    path('Umsatz/', analyzation_sales_view, name='analyzation_sales'),
    path('Kunden/', analyzation_customers_view, name='analyzation_customers'),
    path('Mitarbeiter/', analyzation_employees_view, name='analyzation_employees'),

    url(r'^api/dashboard/chart/data/$', DashboardChartData.as_view(), name='api-dashboard-chart-data'),
    url(r'^api/sales/chart/data/$',     SalesChartData.as_view(),     name='api-sales-chart-data'),
    url(r'^api/customers/chart/data/$', CustomerChartData.as_view(),  name='api-customers-chart-data'),
    url(r'^api/employees/chart/data/$', EmployeeChartData.as_view(),  name='api-employees-chart-data'),
]













   
    
    
   