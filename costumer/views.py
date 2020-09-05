from django.shortcuts import render
from .forms import *

# -------------------------------------------------------------------------
# costumer

# who can access:
    # costumer --> cashbox and administration
# what i need:
    # a list of all the costumers and their information

def costumer_costumer_view(request, *args, **kwargs):
    create_edit_customer_form = FormCreateEditCustomer(request.POST or None)

    context = {
        'form':  create_edit_customer_form

    }
    return render(request, "costumer.html", context)

