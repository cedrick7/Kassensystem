from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response


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
    return render(request, "analyzation_dashboard.html", {})

# for chart.js with rest-framework
class DashboardChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        revenue_labels = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag"]
        revenue_data = [30, 33, 20, 41, 49, 21]

        products_labels = ["Schampoo", "Spülung", "Festiger", "Kamm", "Bürste"]
        products_data = [30, 33, 20, 41, 49]

        services_labels = ["Damen", "Colorationen", "Herren", "Specials", "Kinder"]
        services_data = [30, 33, 20, 41, 49]

        data = {
            "revenue_labels": revenue_labels,
            "revenue_data": revenue_data,
            "products_labels": products_labels,
            "products_data": products_data,
            "services_labels": services_labels,
            "services_data": services_data,
        }
        return Response(data)


def analyzation_sales_view(request, *args, **kwargs):
    return render(request, "analyzation_sales.html", {})


def analyzation_costumers_view(request, *args, **kwargs):
    return render(request, "analyzation_costumers.html", {})


def analyzation_employees_view(request, *args, **kwargs):
    return render(request, "analyzation_employees.html", {})



# ----------------------------------------------------------------------------------------------------------------------
# class DashboardView(View):
#    def get(self, request, *args, **kwargs):
#        return render(request, 'analyzation_dashboard.html', {"customers": 10})


# def get_data(request, *args, **kwargs):
#    data = {
#        "sales": 100,
#        "customers": 10,
#    }
#    return JsonResponse(data) # http response