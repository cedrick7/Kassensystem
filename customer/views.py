from django.shortcuts import render
from .forms import *

# -------------------------------------------------------------------------
# customer

# who can access:
    # customer --> cashbox and administration
# what i need:
    # a list of all the costumers and their information

def customer_customer_view(request, *args, **kwargs):
    create_edit_customer_form = FormCreateEditCustomer(request.POST or None)

    context = {
        'form':  create_edit_customer_form

    }
    return render(request, "customer.html", context)

