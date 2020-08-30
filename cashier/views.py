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

def cashbox_dashboard_view(request, *args, **kwargs):
    return render(request, "cashbox_dashboard.html", {})

def cashbox_pay_view(request, *args, **kwargs):
    return render(request, "cashbox_pay.html", {})

def cashbox_more_view(request, *args, **kwargs):
    return render(request, "cashbox_more.html", {})