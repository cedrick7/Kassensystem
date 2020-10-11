from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

from analyzation.forms import *


# -------------------------------------------------------------------------
# analyzation

# who can access:
# --> analyzation only
# what i need:
# a list of all the


# -------------------------------------------------------------------------
# views:


# DashboardView
def analyzation_dashboard_view(request, *args, **kwargs):
    dateRange_form = FormDashboard(request.POST or None)

    context = {
        'form': dateRange_form
    }
    return render(request, 'analyzation_dashboard.html', context)


# for chart.js with rest-framework
class DashboardChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # chart no.1 - Umsatz Überblick [line-chart]
        revenue_total_data = [26, 39, 44, 64, 92, 64]
        revenue_total_legend = 'Gesamt'
        revenue_products_data = [13, 23, 24, 38, 49, 33]
        revenue_products_legend = 'Produkte'
        revenue_services_data = [13, 16, 20, 26, 43, 31]
        revenue_services_legend = 'Dienstleistungen'
        revenue_chart_legend = 'Umsatz'
        revenue_chart_labels = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag']
        revenue_chart_x_axes = 'Zeit in Tagen'
        revenue_chart_y_axes = 'Umsatz in €'

        # chart no.2 - Produkte Überblick (TOP-X Ranking) [bar-chart]
        products_data = [13, 23, 24, 38, 49, 33]
        products_chart_legend = 'TOP 5 Produkte'
        products_chart_labels = ['Schampoo', 'Spülung', 'Festiger', 'Kamm', 'Bürste']
        products_chart_x_axes = 'Kategoriename'
        products_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'

        # chart no.3 - Dienstleistungen Überblick (TOP-X Ranking) [bar-chart]
        services_data = [13, 16, 20, 26, 43, 31]
        services_chart_legend = 'TOP 5 Dienstleistungen'
        services_chart_labels = ['Damen', 'Colorationen', 'Herren', 'Specials', 'Kinder']
        services_chart_x_axes = 'Kategoriename'
        services_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'

        data = {
            'revenue_total_data': revenue_total_data,
            'revenue_total_legend': revenue_total_legend,
            'revenue_products_data': revenue_products_data,
            'revenue_products_legend': revenue_products_legend,
            'revenue_services_data': revenue_services_data,
            'revenue_services_legend': revenue_services_legend,
            'revenue_chart_legend': revenue_chart_legend,
            'revenue_chart_labels': revenue_chart_labels,
            'revenue_chart_x_axes': revenue_chart_x_axes,
            'revenue_chart_y_axes': revenue_chart_y_axes,
            'products_data': products_data,
            'products_chart_legend': products_chart_legend,
            'products_chart_labels': products_chart_labels,
            'products_chart_x_axes': products_chart_x_axes,
            'products_chart_y_axes': products_chart_y_axes,
            'services_data': services_data,
            'services_chart_legend': services_chart_legend,
            'services_chart_labels': services_chart_labels,
            'services_chart_x_axes': services_chart_x_axes,
            'services_chart_y_axes': services_chart_y_axes
        }
        return Response(data)


# SalesView
def analyzation_sales_view(request, *args, **kwargs):
    sales_form = FormSalesFilter(request.POST or None)

    context = {
        'form': sales_form
    }
    return render(request, 'analyzation_sales.html', context)


# for chart.js with rest-framework
class SalesChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # chart no.1 - Umsatz Überblick [line-chart]
        revenue_total_data = [26, 39, 44, 64, 92, 64]
        revenue_total_legend = 'Gesamt'
        revenue_products_data = [13, 23, 24, 38, 49, 33]
        revenue_products_legend = 'Produkte'
        revenue_services_data = [13, 16, 20, 26, 43, 31]
        revenue_services_legend = 'Dienstleistungen'
        revenue_chart_legend = 'Umsatz'
        revenue_chart_labels = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag']
        revenue_chart_x_axes = 'Zeit in Tagen'
        revenue_chart_y_axes = 'Umsatz in €'

        # chart no.2 - Produkte Überblick (TOP-X Ranking) [bar-chart]
        products_data = [13, 23, 24, 38, 49, 33]
        products_chart_legend = 'TOP 5 Produkte'
        products_chart_labels = ['Schampoo', 'Spülung', 'Festiger', 'Kamm', 'Bürste']
        products_chart_x_axes = 'Kategoriename'
        products_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'

        # chart no.3 - Dienstleistungen Überblick (TOP-X Ranking) [bar-chart]
        services_data = [13, 16, 20, 26, 43, 31]
        services_chart_legend = 'TOP 5 Dienstleistungen'
        services_chart_labels = ['Damen', 'Colorationen', 'Herren', 'Specials', 'Kinder']
        services_chart_x_axes = 'Kategoriename'
        services_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'

        # chart no.4 - Zahlungsmethoden [doughnut-chart]
        payment_data = [60, 35, 5]
        payment_chart_labels = ['Barzahlung', 'Kartenzahlung', 'ApplePay']
        payment_chart_legend = 'Zahlungsmethoden in Prozent'


        # chart no.5 - Stoßzeiten [line-chart]
        peak_times_data = [13, 16, 20, 26, 43, 31, 0]
        peak_times_chart_labels = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
        peak_times_chart_legend = 'Stoßzeiten in Tagen'
        peak_times_chart_x_axes = 'Zeit in Tagen'
        peak_times_chart_y_axes = 'Anzahl der Kunden'

        data = {
            'revenue_total_data': revenue_total_data,
            'revenue_total_legend': revenue_total_legend,
            'revenue_products_data': revenue_products_data,
            'revenue_products_legend': revenue_products_legend,
            'revenue_services_data': revenue_services_data,
            'revenue_services_legend': revenue_services_legend,
            'revenue_chart_legend': revenue_chart_legend,
            'revenue_chart_labels': revenue_chart_labels,
            'revenue_chart_x_axes': revenue_chart_x_axes,
            'revenue_chart_y_axes': revenue_chart_y_axes,
            'products_data': products_data,
            'products_chart_legend': products_chart_legend,
            'products_chart_labels': products_chart_labels,
            'products_chart_x_axes': products_chart_x_axes,
            'products_chart_y_axes': products_chart_y_axes,
            'services_data': services_data,
            'services_chart_legend': services_chart_legend,
            'services_chart_labels': services_chart_labels,
            'services_chart_x_axes': services_chart_x_axes,
            'services_chart_y_axes': services_chart_y_axes,
            'payment_data': payment_data,
            'payment_chart_labels': payment_chart_labels,
            'payment_chart_legend': payment_chart_legend,
            'peak_times_data': peak_times_data,
            'peak_times_chart_labels': peak_times_chart_labels,
            'peak_times_chart_legend': peak_times_chart_legend,
            'peak_times_chart_x_axes': peak_times_chart_x_axes,
            'peak_times_chart_y_axes': peak_times_chart_y_axes
        }
        return Response(data)


# CustomerView
def analyzation_customers_view(request, *args, **kwargs):
    customerForm = FormCustomerFilter(request.POST or None)

    context = {
        'form': customerForm
    }
    return render(request, 'analyzation_customers.html', context)


# for chart.js with rest-framework
class CustomerChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # chart no.1 - Stoßzeiten [line-chart]
        peak_times_data = [13, 16, 20, 26, 43, 31, 0]
        peak_times_chart_labels = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
        peak_times_chart_legend = 'Stoßzeiten in Tagen'
        peak_times_chart_x_axes = 'Zeit in Tagen'
        peak_times_chart_y_axes = 'Anzahl der Kunden'

        # chart no.2 - Kundenart [doughnut-chart]
        customers_data = [60, 40]
        customers_chart_labels = ['Stammkunden', 'Neukunden']
        customers_chart_legend = 'Kundenart in Prozent'

        # chart no.3 - Zahlungsmethode [doughnut-chart]
        payment_data = [60, 35, 5]
        payment_chart_labels = ['Barzahlung', 'Kartenzahlung', 'ApplePay']
        payment_chart_legend = 'Zahlungsmethoden in Prozent'

        # chart no.4 - Produkte Überblick (TOP-X Ranking => generell) [bar-chart]
        products_1_data = [13, 23, 24, 38, 49, 33]
        products_1_chart_legend = 'TOP 5 Produkte (Gesamt)'
        products_1_chart_labels = ['Schampoo', 'Spülung', 'Festiger', 'Kamm', 'Bürste']
        products_1_chart_x_axes = 'Kategoriename'
        products_1_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'

        # chart no.5 - Produkte Überblick (TOP-X Ranking => nach Stammkunden) [bar-chart]
        products_2_data = [13, 23, 24, 38, 49, 33]
        products_2_chart_legend = 'TOP 5 Produkte (nach Stammkunden)'
        products_2_chart_labels = ['Schampoo', 'Spülung', 'Festiger', 'Kamm', 'Bürste']
        products_2_chart_x_axes = 'Kategoriename'
        products_2_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'

        # chart no.6 - Dienstleistungen Überblick (TOP-X Ranking => generell) [bar-chart]
        services_1_data = [13, 16, 20, 26, 43, 31]
        services_1_chart_legend = 'TOP 5 Dienstleistungen (Gesamt)'
        services_1_chart_labels = ['Damen', 'Colorationen', 'Herren', 'Specials', 'Kinder']
        services_1_chart_x_axes = 'Kategoriename'
        services_1_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'

        # chart no.7 - Dienstleistungen Überblick (TOP-X Ranking => nach Stammkunden) [bar-chart]
        services_2_data = [13, 16, 20, 26, 43, 31]
        services_2_chart_legend = 'TOP 5 Dienstleistungen (nach Stammkunden)'
        services_2_chart_labels = ['Damen', 'Colorationen', 'Herren', 'Specials', 'Kinder']
        services_2_chart_x_axes = 'Kategoriename'
        services_2_chart_y_axes = 'Anzahl der Verkäufe pro Kategorie'

        data = {
            'peak_times_data': peak_times_data,
            'peak_times_chart_labels': peak_times_chart_labels,
            'peak_times_chart_legend': peak_times_chart_legend,
            'peak_times_chart_x_axes': peak_times_chart_x_axes,
            'peak_times_chart_y_axes': peak_times_chart_y_axes,
            'customers_data': customers_data,
            'customers_chart_labels': customers_chart_labels,
            'customers_chart_legend': customers_chart_legend,
            'payment_data': payment_data,
            'payment_chart_labels': payment_chart_labels,
            'payment_chart_legend': payment_chart_legend,
            'products_1_data': products_1_data,
            'products_1_chart_legend': products_1_chart_legend,
            'products_1_chart_labels': products_1_chart_labels,
            'products_1_chart_x_axes': products_1_chart_x_axes,
            'products_1_chart_y_axes': products_1_chart_y_axes,
            'products_2_data': products_2_data,
            'products_2_chart_legend': products_2_chart_legend,
            'products_2_chart_labels': products_2_chart_labels,
            'products_2_chart_x_axes': products_2_chart_x_axes,
            'products_2_chart_y_axes': products_2_chart_y_axes,
            'services_1_data': services_1_data,
            'services_1_chart_legend': services_1_chart_legend,
            'services_1_chart_labels': services_1_chart_labels,
            'services_1_chart_x_axes': services_1_chart_x_axes,
            'services_1_chart_y_axes': services_1_chart_y_axes,
            'services_2_data': services_2_data,
            'services_2_chart_legend': services_2_chart_legend,
            'services_2_chart_labels': services_2_chart_labels,
            'services_2_chart_x_axes': services_2_chart_x_axes,
            'services_2_chart_y_axes': services_2_chart_y_axes
        }
        return Response(data)


# EmployeesView
def analyzation_employees_view(request, *args, **kwargs):
    employeesForm = FormEmployeeFilter(request.POST or None)

    context = {
        'form': employeesForm
    }
    return render(request, 'analyzation_employees.html', context)


# for chart.js with rest-framework
class EmployeeChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # chart no.1 - Mitarbeiterzeiten [line-chart]
        employee_times_data = [[0,4,4,4,4,8,8],[8,8,8,8,0,0,0],[2,2,2,2,0,0,8]]
        employee_times_labels = ['Mitarbeitername 1', 'Mitarbeitername 2', 'Mitarbeitername 3']
        employee_times_chart_labels = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
        employee_times_chart_legend = 'Mitarbeiterzeiten'
        employee_times_x_axes = 'Zeit in Tagen'
        employee_times_y_axes = 'Anzahl der Arbeitsstunnden pro Kassierer'

        # chart no.2 - Mitarbeiterumsatz [line-chart]
        employee_revenue_data = [[0,4,4,4,4,8,8],[8,8,8,8,0,0,0],[2,2,2,2,0,0,8]]
        employee_revenue_labels = ['Mitarbeitername 1', 'Mitarbeitername 2', 'Mitarbeitername 3']
        employee_revenue_chart_labels = ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']
        employee_revenue_chart_legend = 'Mitarbeiterumsatz'
        employee_revenue_x_axes = 'Zeit in Tagen'
        employee_revenue_y_axes = 'Anzahl der Arbeitsstunnden pro Kassierer'

        data = {
            'employee_times_data': employee_times_data,
            'employee_times_labels': employee_times_labels,
            'employee_times_chart_labels': employee_times_chart_labels,
            'employee_times_chart_legend': employee_times_chart_legend,
            'employee_times_x_axes': employee_times_x_axes,
            'employee_times_y_axes': employee_times_y_axes,
            'employee_revenue_data': employee_revenue_data,
            'employee_revenue_labels': employee_revenue_labels,
            'employee_revenue_chart_labels': employee_revenue_chart_labels,
            'employee_revenue_chart_legend': employee_revenue_chart_legend,
            'employee_revenue_x_axes': employee_revenue_x_axes,
            'employee_revenue_y_axes': employee_revenue_y_axes
        }
        return Response(data)


# ----------------------------------------------------------------------------------------------------------------------
# class DashboardView(View):
#    def get(self, request, *args, **kwargs):
#        return render(request, 'analyzation_dashboard.html', {'customers': 10})


# def get_data(request, *args, **kwargs):
#    data = {
#        'sales': 100,
#        'customers': 10,
#    }
#    return JsonResponse(data) # http response
