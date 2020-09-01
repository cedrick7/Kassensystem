from django.shortcuts import render
from .forms import *

# -------------------------------------------------------------------------
# cashbox

# who can access:
# --> cashbox only
# what i need:
# a list of all the products + services
# a list of all categories
# a list of all the payment-options

# -------------------------------------------------------------------------
# views:

def cashbox_dashboard_view(request, *args, **kwargs):
    CreateReversalBill = FormCreateReversalBill(request.Post or None)

    context = {
        'form': CreateReversalBill

    }
    return render(request, "cashbox_dashboard.html", context)


def cashbox_pay_view(request, *args, **kwargs):
    return render(request, "cashbox_pay.html", {})


def cashbox_more_view(request, *args, **kwargs):
    return render(request, "cashbox_more.html", {})
