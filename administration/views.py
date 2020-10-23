from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductModelForm, CategoryModelForm, DiscountModelForm, TaxModelForm, AttributeModelForm, CustomerModelForm, EmployeeModelForm, BackupModelForm, PaymenttoolModelForm, SafeModelForm, CashboxModelForm, BillModelForm, ReversalBillModelForm
from product.models import Product, Category, Discount, Tax, Attribute
from customer.models import Customer
from authorization.models import Employee
from administration.models import Backup
from analyzation.models import Worktime
from cashbox.models import Safe, Cashbox, Paymenttool, Bill, Bill_Product, ReversalBill
from django.db import connection 
from django.urls import reverse
import os, subprocess, logging
from pathlib import Path

from django.views.generic import (
    View,
    CreateView, 
    DetailView, 
    ListView, 
    UpdateView,  
    ListView, 
    DeleteView,
)

logger = logging.getLogger('django')



# Administration Dashboard
def administration_dashboard(request, *args, **kwargs):
    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
    file = open(str(os.path.join(BASE_DIR, "static", "syslog")), 'r')
    lines = file.readlines()

    loglist = []
    for line in lines:
       loglist.append(line)

    context = {
            "loglist":loglist
        }
    return render(request, "new/administration_dashboard_copy.html", context)

# Produkte
class ProductListView(ListView):
    template_name = 'new/administration_products_copy.html'
    queryset = Product.objects.all()

class ProductCreateView(View):
    template_name = 'new/administration_products_create-update_copy.html'

    # http/GET method
    def get(self, request, *args, **kwargs):
        form = ProductModelForm()
        context = {
            "form":form,
            "headline": "Erstelle ein Produkt"
        }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, *args, **kwargs):
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('Produkt wurde erfolgreich angelegt')
            return redirect('administration:product_list')
        context = {
            "form":form
        }
        return render(request, self.template_name, context)

class ProductUpdateView(View):
    template_name = 'new/administration_products_create-update_copy.html'

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None: 
            obj = get_object_or_404(Product, id=id)
        return obj

    # http/GET method
    def get(self, request, id=None, *args, **kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = ProductModelForm(instance=obj)
            context={
                "object":obj,
                "form":form, 
                "headline":"Bearbeite ein Produkt"
            }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, id=None, *args, **kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = ProductModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                logger.info('Produkt wurde erfolgreich geändert')
                return redirect('administration:product_list')
                context={
                        "object":obj,
                        "form":form
                    }
        return render(request, self.template_name, context)

class ProductDeleteView(DeleteView):
    template_name = 'new/administration_products_delete_copy.html'
    queryset = Product.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Product, id=id_)

    def get_success_url(self):
        return reverse('administration:product_list')

    def post(self, request, id=None, *args, **kwargs):
        
        context = {}    

        obj = self.get_object()
        if obj is not None:
            obj.delete()
            logger.info('Produkt wurde erfolgreich gelöscht')

            return redirect('administration:product_list')
        return render(request, self.template_name, context)



# Kategorien
class CategoryListView(ListView):
    template_name = 'new/administration_categories_copy.html'
    queryset = Category.objects.all()

class CategoryCreateView(View):
    template_name = 'new/administration_categories_create-update_copy.html'

    # http/GET method
    def get(self, request, *args, **kwargs):
        form = CategoryModelForm()
        context = {
            "form":form,
            "headline": "Erstelle eine Kategorie"
        }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, *args, **kwargs):
        form = CategoryModelForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('Kategorie wurde erfolgreich angelegt')
            return redirect('administration:category_list')
        context = {
            "form":form
        }
        return render(request, self.template_name, context)

class CategoryUpdateView(View):
    template_name = 'new/administration_categories_create-update_copy.html'

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None: 
            obj = get_object_or_404(Category, id=id)
        return obj

    # http/GET method
    def get(self, request, id=None, *args, **kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = CategoryModelForm(instance=obj)
            context={
                "object":obj,
                "form":form, 
                "headline":"Bearbeite eine Kategorie"
            }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, id=None, *args, **kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = CategoryModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                logger.info('Kategorie wurde erfolgreich geändert')
                return redirect('administration:category_list')
                context={
                        "object":obj,
                        "form":form
                    }
        return render(request, self.template_name, context)

class CategoryDeleteView(DeleteView):
    template_name = 'new/administration_categories_delete_copy.html'
    queryset = Category.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Category, id=id_)

    def get_success_url(self):
        return reverse('administration:category_list')

    def post(self, request, id=None, *args, **kwargs):
        
        context = {}    

        obj = self.get_object()
        if obj is not None:
            obj.delete()
            logger.info('Kategorie wurde erfolgreich gelöscht')

            return redirect('administration:category_list')


# Rabatte
class DiscountListView(ListView):
    template_name = 'new/administration_discounts_copy.html'
    queryset = Discount.objects.all()

class DiscountCreateView(View):
    template_name = 'new/administration_discounts_create-update_copy.html'

    # http/GET method
    def get(self, request, *args, **kwargs):
        form = DiscountModelForm()
        context = {
            "form":form,
            "headline": "Erstelle ein Rabatt"
        }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, *args, **kwargs):
        form = DiscountModelForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('Rabatt wurde erfolgreich angelegt')
            return redirect('administration:discount_list')
        context = {
            "form":form
        }
        return render(request, self.template_name, context)

class DiscountUpdateView(View):
    template_name = 'new/administration_discounts_create-update_copy.html'

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None: 
            obj = get_object_or_404(Discount, id=id)
        return obj

    # http/GET method
    def get(self, request, id=None, *args, **kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = DiscountModelForm(instance=obj)
            context={
                "object":obj,
                "form":form, 
                "headline":"Bearbeite ein Rabatt"
            }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, id=None, *args, **kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = DiscountModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                logger.info('Rabatt wurde erfolgreich geändert')
                return redirect('administration:discount_list')
                context={
                        "object":obj,
                        "form":form
                    }
        return render(request, self.template_name, context)

class DiscountDeleteView(DeleteView):
    template_name = 'new/administration_discounts_delete_copy.html'
    queryset = Discount.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Discount, id=id_)

    def get_success_url(self):
        return reverse('administration:discount_list')

    def post(self, request, id=None, *args, **kwargs):
        
        context = {}    

        obj = self.get_object()
        if obj is not None:
            obj.delete()
            logger.info('Rabatt wurde erfolgreich gelöscht')

            return redirect('administration:discount_list')


# Steuersätze
class TaxListView(ListView):
    template_name = 'new/administration_taxes_copy.html'
    queryset = Tax.objects.all()

class TaxCreateView(View):
    template_name = 'new/administration_taxes_create-update_copy.html'

    # http/GET method
    def get(self, request, *args, **kwargs):
        form = TaxModelForm()
        context = {
            "form":form,
            "headline": "Erstelle einen Steuersatz"
        }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, *args, **kwargs):
        form = TaxModelForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('Steuersatz wurde erfolgreich angelegt')
            return redirect('administration:tax_list')
        context = {
            "form":form
        }
        return render(request, self.template_name, context)

class TaxUpdateView(View):
    template_name = 'new/administration_taxes_create-update_copy.html'

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None: 
            obj = get_object_or_404(Tax, id=id)
        return obj

    # http/GET method
    def get(self, request, id=None, *args, **kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = TaxModelForm(instance=obj)
            context={
                "object":obj,
                "form":form, 
                "headline":"Bearbeite einen Steuersatz"
            }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, id=None, *args, **kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = TaxModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                logger.info('Steuersatz wurde erfolgreich geändert')
                return redirect('administration:tax_list')
                context={
                        "object":obj,
                        "form":form
                    }
        return render(request, self.template_name, context)

class TaxDeleteView(DeleteView):
    template_name = 'new/administration_taxes_delete_copy.html'
    queryset = Tax.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Tax, id=id_)

    def get_success_url(self):
        return reverse('administration:tax_list')

    def post(self, request, id=None, *args, **kwargs):
        
        context = {}    

        obj = self.get_object()
        if obj is not None:
            obj.delete()
            logger.info('Steuersatz wurde erfolgreich gelöscht')

            return redirect('administration:tax_list')


# Attribute 
class AttributeListView(ListView):
    template_name = 'new/administration_attributes_copy.html'
    queryset = Attribute.objects.all()

class AttributeCreateView(View):
    template_name = 'new/administration_attributes_create-update_copy.html'

    # http/GET method
    def get(self, request, *args, **kwargs):
        form = AttributeModelForm()
        context = {
            "form":form,
            "headline": "Erstelle ein Attribut"
        }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, *args, **kwargs):
        form = AttributeModelForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('Attribut wurde erfolgreich angelegt')
            return redirect('administration:attribute_list')
        context = {
            "form":form
        }
        return render(request, self.template_name, context)

class AttributeUpdateView(View):
    template_name = 'new/administration_attributes_create-update_copy.html'

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None: 
            obj = get_object_or_404(Attribute, id=id)
        return obj

    # http/GET method
    def get(self, request, id=None, *args, **kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = AttributeModelForm(instance=obj)
            context={
                "object":obj,
                "form":form, 
                "headline":"Bearbeite einen Steuersatz"
            }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, id=None, *args, **kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = AttributeModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                logger.info('Attribut wurde erfolgreich geändert')
                return redirect('administration:attribute_list')
                context={
                        "object":obj,
                        "form":form
                    }
        return render(request, self.template_name, context)

class AttributeDeleteView(DeleteView):
    template_name = 'new/administration_attributes_delete_copy.html'
    queryset = Attribute.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Attribute, id=id_)

    def get_success_url(self):
        return reverse('administration:attribute_list')

    def post(self, request, id=None, *args, **kwargs):
        
        context = {}    

        obj = self.get_object()
        if obj is not None:
            obj.delete()
            logger.info('Attribut wurde erfolgreich gelöscht')

            return redirect('administration:attributes_list')


# Kunden
class CustomerListView(ListView):
    template_name = 'new/administration_customers_copy.html'
    queryset = Customer.objects.all()

class CustomerCreateView(View):
    template_name = 'new/administration_customers_create-update_copy.html'

    # http/GET method
    def get(self, request, *args, **kwargs):
        form = CustomerModelForm()
        context = {
            "form":form,
            "headline": "Erstelle einen Kunden"
        }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, id=None, *args, **kwargs):
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('Kunde wurde erfolgreich angelegt')
            return redirect('administration:customer_list')
        context = {
            "form":form
        }
        return render(request, self.template_name, context)

class CustomerUpdateView(View):
    template_name = 'new/administration_customers_create-update_copy.html'

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None: 
            obj = get_object_or_404(Customer, id=id)
        return obj

    # http/GET method
    def get(self, request, id=None, *args, **kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = CustomerModelForm(instance=obj)
            context={
                "object":obj,
                "form":form, 
                "headline":"Bearbeite einen Kunden"
            }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, id=None, *args, **kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = CustomerModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                logger.info('Kunde wurde erfolgreich geändert')
                return redirect('administration:customer_list')
                context={
                        "object":obj,
                        "form":form
                    }
        return render(request, self.template_name, context)

class CustomerDeleteView(DeleteView):
    template_name = 'new/administration_customers_delete_copy.html'
    queryset = Customer.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Customer, id=id_)

    def get_success_url(self):
        return reverse('administration:customer_list')

    def post(self, request, id=None, *args, **kwargs):
        
        context = {}    

        obj = self.get_object()
        if obj is not None:
            obj.delete()
            logger.info('Kunde wurde erfolgreich gelöscht')

            return redirect('administration:customer_list')


# Angestellte
class EmployeeListView(ListView):
    template_name = 'new/administration_employees_copy.html'
    queryset = Employee.objects.all()

class EmployeeUpdateView(View):
    template_name = 'new/administration_employees_create-update_copy.html'

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None: 
            obj = get_object_or_404(Employee, id=id)
        return obj

    # http/GET method
    def get(self, request, id=None, *args, **kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = EmployeeModelForm(instance=obj)
            context={
                "object":obj,
                "form":form, 
                "headline":"Bearbeite einen Mitarbeiter"
            }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, id=None, *args, **kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = EmployeeModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                logger.info('Mitarbeiter wurde erfolgreich geändert')
                return redirect('administration:employee_list')
                context={
                        "object":obj,
                        "form":form
                    }
        return render(request, self.template_name, context)

class EmployeeDeleteView(DeleteView):
    template_name = 'new/administration_employees_delete_copy.html'
    queryset = Employee.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Employee, id=id_)

    def get_success_url(self):
        return reverse('administration:employee_list')

    def post(self, request, id=None, *args, **kwargs):
        
        context = {}    

        obj = self.get_object()
        if obj is not None:
            obj.delete()
            logger.info('Mitarbeiter wurde erfolgreich gelöscht')

            return redirect('administration:employee_list')


# Arbeitszeit
class WorkTimeListView(ListView):
    template_name = 'new/administration_worktime_copy.html'
    queryset = Worktime.objects.all()


# Safe
class SafeListView(ListView):
    template_name = 'new/administration_safes_copy.html'
    queryset = Safe.objects.all()

class SafeCreateView(View):
    template_name = 'new/administration_safes_create-update_copy.html'

    # http/GET method
    def get(self, request, *args, **kwargs):
        form = SafeModelForm()
        context = {
            "form":form,
            "headline": "Erstelle einen Safe"
        }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, *args, **kwargs):
        form = SafeModelForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('Tresor wurde erfolgreich angelegt')
            return redirect('administration:safe_list')
        context = {
            "form":form
        }
        return render(request, self.template_name, context)

class SafeUpdateView(View):
    template_name = 'new/administration_safes_create-update_copy.html'

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None: 
            obj = get_object_or_404(Safe, id=id)
        return obj

    # http/GET method
    def get(self, request, id=None, *args, **kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = SafeModelForm(instance=obj)
            context={
                "object":obj,
                "form":form, 
                "headline":"Bearbeite einen Tresor"
            }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, id=None, *args, **kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = SafeModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                logger.info('Tresor wurde erfolgreich geändert')
                return redirect('administration:safe_list')
                context={
                        "object":obj,
                        "form":form
                    }
        return render(request, self.template_name, context)

class SafeDeleteView(DeleteView):
    template_name = 'new/administration_safes_delete_copy.html'
    queryset = Safe.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Safe, id=id_)

    def get_success_url(self):
        return reverse('administration:safe_list')

    def post(self, request, id=None, *args, **kwargs):
        
        context = {}    

        obj = self.get_object()
        if obj is not None:
            obj.delete()
            logger.info('Tresor wurde erfolgreich gelöscht')

            return redirect('administration:safe_list')

# Kasse
class CashboxListView(ListView):
    template_name = 'new/administration_cashboxes_copy.html'
    queryset = Cashbox.objects.all()

class CashboxCreateView(View):
    template_name = 'new/administration_cashboxes_create-update_copy.html'

    # http/GET method
    def get(self, request, *args, **kwargs):
        form = CashboxModelForm()
        context = {
            "form":form,
            "headline": "Erstelle eine Kasse"
        }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, *args, **kwargs):
        form = CashboxModelForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('Kasse wurde erfolgreich angelegt')
            return redirect('administration:cashbox_list')
        context = {
            "form":form
        }
        return render(request, self.template_name, context)

class CashboxUpdateView(View):
    template_name = 'new/administration_cashboxes_create-update_copy.html'

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None: 
            obj = get_object_or_404(Cashbox, id=id)
        return obj

    # http/GET method
    def get(self, request, id=None, *args, **kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = CashboxModelForm(instance=obj)
            context={
                "object":obj,
                "form":form, 
                "headline":"Bearbeite eine Kasse"
            }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, id=None, *args, **kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = CashboxModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                logger.info('Kasse wurde erfolgreich geändert')
                return redirect('administration:cashbox_list')
                context={
                        "object":obj,
                        "form":form
                    }
        return render(request, self.template_name, context)        

class CashboxDeleteView(DeleteView):
    template_name = 'new/administration_cashboxes_delete_copy.html'
    queryset = Cashbox.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Cashbox, id=id_)

    def get_success_url(self):
        return reverse('administration:cashbox_list')

    def post(self, request, id=None, *args, **kwargs):
        
        context = {}    

        obj = self.get_object()
        if obj is not None:
            obj.delete()
            logger.info('Kasse wurde erfolgreich gelöscht')

            return redirect('administration:cashbox_list')


# Zahlungsmittel
class PaymenttoolListView(ListView):
    template_name = 'new/administration_paymenttools_copy.html'
    queryset = Paymenttool.objects.all()

class PaymenttoolCreateView(View):
    template_name = 'new/administration_paymenttools_create-update_copy.html'

    # http/GET method
    def get(self, request, *args, **kwargs):
        form = PaymenttoolModelForm()
        context = {
            "form":form,
            "headline": "Erstelle einen Zahlungsmittel"
        }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, *args, **kwargs):
        form = PaymenttoolModelForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('Zahlungsmittel wurde erfolgreich angelegt')
            return redirect('administration:paymenttool_list')
        context = {
            "form":form
        }
        return render(request, self.template_name, context)

class PaymenttoolUpdateView(View):
    template_name = 'new/administration_paymenttools_create-update_copy.html'

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None: 
            obj = get_object_or_404(Paymenttool, id=id)
        return obj

    # http/GET method 
    def get(self, request, id=None, *args, **kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = PaymenttoolModelForm(instance=obj)
            context={
                "object":obj,
                "form":form, 
                "headline":"Bearbeite ein Zahlungsmittel"
            }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, id=None, *args, **kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = PaymenttoolModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                logger.info('Zahlungsmittel wurde erfolgreich geändert')
                return redirect('administration:paymenttool_list')
                context={
                        "object":obj,
                        "form":form
                    }
        return render(request, self.template_name, context)

class PaymenttoolDeleteView(DeleteView):
    template_name = 'new/administration_paymenttools_delete_copy.html'
    queryset = Paymenttool.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Paymenttool, id=id_)

    def get_success_url(self):
        return reverse('administration:paymenttool_list')

    def post(self, request, id=None, *args, **kwargs):
        
        context = {}    

        obj = self.get_object()
        if obj is not None:
            obj.delete()
            logger.info('Zahlungsmittel wurde erfolgreich gelöscht')

            return redirect('administration:paymenttool_list')
    


# Backups
class BackupListView(ListView):
    template_name = 'new/administration_backups_copy.html'
    queryset = Backup.objects.all()

class BackupCreateView(View):
    template_name = 'new/administration_backups_create-update_copy.html'

    def custom_sql(self, query):
        with connection.cursor() as cursor:
            cursor.execute(query, [self.path])
            row = cursor.fetchone()
        return row

    def createBackup(self, pk):
        file = "backup.sh"
        BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
        path = os.path.join(BASE_DIR, 'static/scripts/')
        exec = path + file
        print("Pk des Backups:")
        print(pk)
        # subprocess.run(["sh", exec])

        backup = os.path.join(BASE_DIR, 'static/backups/' + str(7) + '/sql.dumb')    #str(pk)
        
        sql_query = "UPDATE TABLE Backup SET path = " + backup + " WHERE id = " + str(pk) + ";"
        print(sql_query)
        # Backup.objects.raw(sql_query)
        row = self.custom_sql(sql_query)
        print(row)



    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None: 
            obj = get_object_or_404(Backup, id=id)
        return obj


    # http/GET method
    def get(self, request, *args, **kwargs):
        form = BackupModelForm()
        context = {
            "form":form,
            "headline": "Erstelle einen Datensicherungssatz"
        }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, *args, **kwargs):
        form = BackupModelForm(request.POST)
        if form.is_valid():
            # backup = form.save()     
            # pk = backup.pk
            # self.createBackup(pk)
            # logger.info('Datensicherungssatz wurde erfolgreich angelegt')

            return redirect('administration:backup_list')
        context = {
            "form":form
        }
        return render(request, self.template_name, context)

class BackupUpdateView(View):
    template_name = 'new/administration_backups_create-update_copy.html'

    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None: 
            obj = get_object_or_404(Backup, id=id)
        return obj

    # http/GET method
    def get(self, request, id=None, *args, **kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = BackupModelForm(instance=obj)
            context={
                "object":obj,
                "form":form, 
                "headline":"Bearbeite einen Datensicherungssatz"
            }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, id=None, *args, **kwargs):
        context={}
        obj = self.get_object()
        if obj is not None:
            form = BackupModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                logger.info('Datensicherungssatz wurde erfolgreich geändert')
                return redirect('administration:backup_list')
                context={
                        "object":obj,
                        "form":form
                    }
        return render(request, self.template_name, context)

class BackupDeleteView(DeleteView):
    template_name = 'new/administration_backups_delete_copy.html'
    queryset = Backup.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Backup, id=id_)

    def get_success_url(self):
        return reverse('administration:backup_list')

    def post(self, request, id=None, *args, **kwargs):
        
        context = {}    

        obj = self.get_object()
        if obj is not None:
            obj.delete()
            logger.info('Datensicherungssatz wurde erfolgreich gelöscht')

            return redirect('administration:backup_list')


# Rechnungen 
class BillListView(ListView):
    template_name = 'new/administration_bills_copy.html'
    queryset = Bill.objects.all()

class BillDetailView(View):
    template_name = 'new/administration_bills_detail_copy.html'

    # http/GET method
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(Bill, id=id)
            billproductIdlist = Bill_Product.objects.filter(bill=id).values_list('product', flat=True)
            productlist = []

            for i in billproductIdlist:
                p = Product.objects.get(id=i)
                productlist.append(p)

            context = {
                "object":obj,
                "productlist":productlist    
                
            }
            
        return render(request, self.template_name, context)

class BillCreateView(View):
    template_name = 'new/administration_bills_create-update_copy_löschen.html'

    # http/GET method
    def get(self, request, *args, **kwargs):
        form = BillModelForm()
        context = {
            "form":form,
            "headline": "Erstelle eine Rechnung"
        }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, *args, **kwargs):
        form = BillModelForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('Rechnung wurde erfolgreich angelegt')
            return redirect('administration:bill_list')
        context = {
            "form":form
        }
        return render(request, self.template_name, context)


# Stornorechnungen 
class ReversalBillListView(ListView):
    template_name = 'new/administration_reversalbills_copy.html'
    queryset = ReversalBill.objects.all()

class ReversalBillDetailView(View):
    template_name = 'new/administration_reversalbills_detail_copy.html'

    # http/GET method
    def get(self, request, id=None, *args, **kwargs):
        context = {}
        if id is not None:
            obj = get_object_or_404(ReversalBill, id=id)
            billIdlist = ReversalBill.objects.filter(bill=id).values_list('bill', flat=True)
            billlist = []

            for i in billIdlist:
                b = Bill.objects.get(id=i)
                billlist.append(b)
                
            context = {
                "object":obj,
                "billlist":billlist    
                
            }

        return render(request, self.template_name, context)

class ReversalBillCreateView(View):
    template_name = 'new/administration_reversalbills_create-update_copy_löschen.html'

    # http/GET method
    def get(self, request, *args, **kwargs):
        form = ReversalBillModelForm()
        context = {
            "form":form,
            "headline": "Erstelle eine Stornorechnung"
        }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, *args, **kwargs):
        form = ReversalBillModelForm(request.POST)
        if form.is_valid():
            form.save()
            logger.info('Stornorechnung wurde erfolgreich angelegt')
            return redirect('administration:reversalbill_list')
        context = {
            "form":form
        }
        return render(request, self.template_name, context)









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







# def productlist_view(request, *args, **kwargs):
    
#     queryset=Product.objects.all()
    
#     context = {
#         'object_list': queryset
#     }

#     return render(request, "test_productlist.html", context)


# def productdetail_view(request, id):
    
#     queryset=Product.objects.get(id=id)
    
#     context = {
#         'object': queryset
#     }

#     return render(request, "test_productdetail.html", context)






# --------------------------------------------------------------------------------

# def administration_dashboard_view(request, *args, **kwargs):
#     return render(request, "administration_dashboard.html", {})


# # !!! Please do a searchbar function for this view as mentioned in discord  !!!
# # I need the following:
# # returntype= list  filteredobject= title,brand,attributes,category




# def administration_products_view(request, *args, **kwargs):
    
#     queryset=Product.objects.all()
#     #print(type(queryset))
#     #for i in queryset:
#     #    print(i.title)
    
#     context = {
#         'products': queryset
#     }

#     return render(request, "administration_products.html", context)

# def administration_products_detail_view(request, id,  *args, **kwargs):
#     create_edit_products_form = FormCreateEditProducts(request.POST or None)
    
#     print(id)
#     object = Product.objects.get(id=id)
#     print(object)
    
#     context = {
#         'form': create_edit_products_form,
#         'object': object 
#     }
#     return render(request, "administration_products_detail.html", context)

# def administration_services_view(request, *args, **kwargs):
#     return render(request, "administration_services.html", {})

# def administration_services_detail_view(request, *args, **kwargs):
#     create_edit_services_form = FormCreateEditServices(request.POST or None)

#     context = {
#         'form': create_edit_services_form
#     }

#     return render(request, "administration_services_detail.html", context)

# def administration_categories_view(request, *args, **kwargs):
#     return render(request, "administration_categories.html", {})

# def administration_categories_detail_view(request, *args, **kwargs):
#     create_edit_categories_form = FormCreateEditCategory(request.POST or None)

#     context = {
#         'form': create_edit_categories_form
#     }
#     return render(request, "administration_categories_detail.html", context)

# def administration_attributes_view(request, *args, **kwargs):
#     return render(request, "administration_attributes.html", {})

# def administration_attributes_detail_view(request, *args, **kwargs):
#     create_edit_properties_form = FormCreateEditProperties(request.POST or None)

#     context = {
#         'form': create_edit_properties_form
#     }

#     return render(request, "administration_attributes_detail.html", context)

# def administration_discounts_view(request, *args, **kwargs):
#     return render(request, "administration_discounts.html", {})

# def administration_discounts_detail_view(request, *args, **kwargs):
#     create_edit_discount_form = FormCreateEditDiscount(request.POST or None)

#     context = {
#         'form': create_edit_discount_form
#     }
#     return render(request, "administration_discounts_detail.html", context)

# def administration_employees_view(request, *args, **kwargs):
#     return render(request, "administration_employees.html", {})

# def administration_employees_detail_view(request, *args, **kwargs):
#     create_edit_employee_form = FormCreateEditEmployee(request.POST or None)

#     context = {
#         'form': create_edit_employee_form
#     }
#     return render(request, "administration_employees_detail.html", context)

# def administration_invoices_view(request, *args, **kwargs):
#     return render(request, "administration_invoices.html", {})

# def administration_invoices_detail_view(request, *args, **kwargs):
#     create_edit_invoices_form = FromCreateEditInvoices(request.POST or None)

#     context = {
#         'form': create_edit_invoices_form
#     }
#     return render(request, "administration_invoices_detail.html", context)

# def administration_cashboxes_view(request, *args, **kwargs):
#     create_edit_cashbox_form = FormCreateEditCashbox(request.POST or None)

#     context = {
#         'form': create_edit_cashbox_form
#     }
#     return render(request, "administration_cashboxes.html", context)

# def administration_safes_view(request, *args, **kwargs):
#     create_edit_safe_form = FormCreateEditSafe(request.POST or None)

#     context = {
#         'form': create_edit_safe_form
#     }
#     return render(request, "administration_safes.html", context)

# def administration_backups_view(request, *args, **kwargs):
#     return render(request, "administration_backups.html", {})

# def administration_backups_detail_view(request, *args, **kwargs):
#     create_edit_backup_form = FormCreateEditBackup(request.POST or None)

#     context = {
#         'form': create_edit_backup_form
#     }
#     return render(request, "administration_backups_detail.html", context)

# def administration_payments_view(request, *args, **kwargs):
#     create_edit_payment_form = FormCreateEditPayment(request.POST or None)

#     context = {
#         'form': create_edit_payment_form
#     }
#     return render(request, "administration_payments.html", context)

# def administration_requests_view(request, *args, **kwargs):
#     return render(request, "administration_requests.html", {})
