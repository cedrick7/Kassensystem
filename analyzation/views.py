from django.shortcuts import render

# -------------------------------------------------------------------------
# analyzation

# who can access:
    # --> analyzation only
# what i need:
    # a list of all the

# -------------------------------------------------------------------------
# views:

def analyzation_dashboard_view(request, *args, **kwargs):
    return render(request, "analyzation_dashboard.html", {})

def analyzation_sales_view(request, *args, **kwargs):
    return render(request, "analyzation_sales.html", {})

def analyzation_costumers_view(request, *args, **kwargs):
    return render(request, "analyzation_costumers.html", {})

def analyzation_employees_view(request, *args, **kwargs):
    return render(request, "analyzation_employees.html", {})
