from django.shortcuts import render

# -------------------------------------------------------------------------
# costumer

# who can access:
    # costumer --> cashier and admin
# what i need:
    # a list of all the costumers and their information

def costumer_costumer_view(request, *args, **kwargs):
    return render(request, "costumer.html", {})
