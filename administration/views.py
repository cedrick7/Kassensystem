from django.shortcuts import render
from .forms import *
# -------------------------------------------------------------------------
# administration

# who can access:
    # --> administration only
# what i need:
    # a list of all the products
    # a list of all the services
    # a list of all the categories
    # a list of all the attributes
    # a list of all the discounts
    # a list of all the employees with their information
    # a list of all the invoices with their information
    # a list of all the cashboxes and their online/offline-status + money in there
    # a list of all the safes and their online/offline-status + money in there
    # a list of all the backups with their information
    # a list of all the payment-options
    # a list of all the requests + a way to handle them

# -------------------------------------------------------------------------
# views:

def administration_dashboard_view(request, *args, **kwargs):
    return render(request, "administration_dashboard.html", {})

def administration_products_view(request, *args, **kwargs):
    
    queryset=Product.objects.all()
    print(type(queryset))

    for i in queryset:
        print(i.title)
    
    context = {
        'products': queryset
    }

    return render(request, "administration_products.html", context)

def administration_products_detail_view(request, id,  *args, **kwargs):
    create_edit_products_form = FormCreateEditProducts(request.POST or None)
    
    print(id)
    object = Product.objects.get(id=id)
    print(object)
    
    context = {
        'form': create_edit_products_form,
        'object': object 
    }
    return render(request, "administration_products_detail.html", context)

def administration_services_view(request, *args, **kwargs):
    return render(request, "administration_services.html", {})

def administration_services_detail_view(request, *args, **kwargs):
    return render(request, "administration_services_detail.html", {})

def administration_categories_view(request, *args, **kwargs):
    return render(request, "administration_categories.html", {})

def administration_categories_detail_view(request, *args, **kwargs):
    create_edit_categories_form = FormCreateEditCategory(request.POST or None)

    context = {
        'form': create_edit_categories_form
    }
    return render(request, "administration_categories_detail.html", context)

def administration_attributes_view(request, *args, **kwargs):
    return render(request, "administration_attributes.html", {})

def administration_attributes_detail_view(request, *args, **kwargs):
    create_edit_properties_form = FormCreateEditProperties(request.POST or None)

    context = {
        'form': create_edit_properties_form
    }

    return render(request, "administration_attributes_detail.html", context)

def administration_discounts_view(request, *args, **kwargs):
    return render(request, "administration_discounts.html", {})

def administration_discounts_detail_view(request, *args, **kwargs):
    create_edit_discount_form = FormCreateEditDiscount(request.POST or None)

    context = {
        'form': create_edit_discount_form
    }
    return render(request, "administration_discounts_detail.html", context)

def administration_employees_view(request, *args, **kwargs):
    return render(request, "administration_employees.html", {})

def administration_employees_detail_view(request, *args, **kwargs):
    create_edit_employee_form = FormCreateEditEmployee(request.POST or None)

    context = {
        'form': create_edit_employee_form
    }
    return render(request, "administration_employees_detail.html", context)

def administration_invoices_view(request, *args, **kwargs):
    return render(request, "administration_invoices.html", {})

def administration_invoices_detail_view(request, *args, **kwargs):
    return render(request, "administration_invoices_detail.html", {})

def administration_cashboxes_view(request, *args, **kwargs):
    create_edit_cashbox_form = FormCreateEditCashbox(request.POST or None)

    context = {
        'form': create_edit_cashbox_form
    }
    return render(request, "administration_cashboxes.html", context)

def administration_safes_view(request, *args, **kwargs):
    create_edit_safe_form = FormCreateEditSafe(request.POST or None)

    context = {
        'form': create_edit_safe_form
    }
    return render(request, "administration_safes.html", context)

def administration_backups_view(request, *args, **kwargs):
    return render(request, "administration_backups.html", {})

def administration_backups_detail_view(request, *args, **kwargs):
    create_edit_backup_form = FormCreateEditBackup(request.POST or None)

    context = {
        'form': create_edit_backup_form
    }
    return render(request, "administration_backups_detail.html", context)

def administration_payments_view(request, *args, **kwargs):
    create_edit_payment_form = FormCreateEditPayment(request.POST or None)

    context = {
        'form': create_edit_payment_form
    }
    return render(request, "administration_payments.html", context)

def administration_requests_view(request, *args, **kwargs):
    return render(request, "administration_requests.html", {})
