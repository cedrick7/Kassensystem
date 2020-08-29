from django.shortcuts import render

# -------------------------------------------------------------------------
# admin

# who can access:
    # --> admin only
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

def admin_dashboard_view(request, *args, **kwargs):
    return render(request, "admin_dashboard.html", {})

def admin_products_view(request, *args, **kwargs):
    return render(request, "admin_products.html", {})

def admin_products_detail_view(request, *args, **kwargs):
    return render(request, "admin_products_detail.html", {})

def admin_services_view(request, *args, **kwargs):
    return render(request, "admin_services.html", {})

def admin_services_detail_view(request, *args, **kwargs):
    return render(request, "admin_services_detail.html", {})

def admin_categories_view(request, *args, **kwargs):
    return render(request, "admin_categories.html", {})

def admin_categories_detail_view(request, *args, **kwargs):
    return render(request, "admin_categories_detail.html", {})

def admin_attributes_view(request, *args, **kwargs):
    return render(request, "admin_attributes.html", {})

def admin_attributes_detail_view(request, *args, **kwargs):
    return render(request, "admin_attributes_detail.html", {})

def admin_discounts_view(request, *args, **kwargs):
    return render(request, "admin_discounts.html", {})

def admin_discounts_detail_view(request, *args, **kwargs):
    return render(request, "admin_discounts_detail.html", {})

def admin_employees_view(request, *args, **kwargs):
    return render(request, "admin_employees.html", {})

def admin_employees_detail_view(request, *args, **kwargs):
    return render(request, "admin_employees_detail.html", {})

def admin_invoices_view(request, *args, **kwargs):
    return render(request, "admin_invoices.html", {})

def admin_invoices_detail_view(request, *args, **kwargs):
    return render(request, "admin_invoices_detail.html", {})

def admin_cashboxes_view(request, *args, **kwargs):
    return render(request, "admin_cashboxes.html", {})

def admin_safes_view(request, *args, **kwargs):
    return render(request, "admin_safes.html", {})

def admin_backups_view(request, *args, **kwargs):
    return render(request, "admin_backups.html", {})

def admin_backups_detail_view(request, *args, **kwargs):
    return render(request, "admin_backups_detail.html", {})

def admin_payments_view(request, *args, **kwargs):
    return render(request, "admin_payments.html", {})

def admin_requests_view(request, *args, **kwargs):
    return render(request, "admin_requests.html", {})
