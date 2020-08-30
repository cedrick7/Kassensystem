from django.shortcuts import render

# -------------------------------------------------------------------------
# cashier

# who can access:
    # --> cashier only
# what i need:
    # a list of all the products + services
    # a list of all categories
    # a list of all the payment-options

# -------------------------------------------------------------------------
# views:

def cashier_dashboard_view(request, *args, **kwargs):
    return render(request, "cashier_dashboard.html", {})

def cashier_pay_view(request, *args, **kwargs):
    return render(request, "cashier_pay.html", {})

def cashier_more_view(request, *args, **kwargs):
    return render(request, "cashier_more.html", {})
