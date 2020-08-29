from django.shortcuts import render

# -------------------------------------------------------------------------
# analyst

# who can access:
    # --> analyst only
# what i need:
    # a list of all the

# -------------------------------------------------------------------------
# views:

def analyst_dashboard_view(request, *args, **kwargs):
    return render(request, "analyst_dashboard.html", {})

def analyst_sales_view(request, *args, **kwargs):
    return render(request, "analyst_sales.html", {})

def analyst_costumers_view(request, *args, **kwargs):
    return render(request, "analyst_costumers.html", {})

def analyst_employees_view(request, *args, **kwargs):
    return render(request, "analyst_employees.html", {})
