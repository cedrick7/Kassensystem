from django.shortcuts import render
from .forms import *
from product.models import Product

from django.views.generic import (
    View,
    ListView,

)

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




class cashbox_dashboard_view(View):
    template_name = 'new/cashbox_dashboard_copy.html'

    # def get_object(self):
    #     id = self.kwargs.get('id')
    #     obj = None
    #     if id is not None: 
    #         obj = get_object_or_404(Product, id=id)
    #     return obj

    # http/GET method
    def get(self, request, id=None, *args, **kwargs):
        context={}
        queryset = Product.objects.all()
        # obj = self.get_object()
        # if obj is not None:
            # form = BackupModelForm(instance=obj)
        context={
            "object_list":queryset,
            # "object":obj,
            # "form":form, 
            # "headline":"Bearbeite einen Datensicherungssatz"
        }
        return render(request, self.template_name, context)

    
    # http/POST method
    def post(self, request, id=None, *args, **kwargs):
        context={}
        print("Hallo")
        # obj = self.get_object()
        # if obj is not None:
        #     form = BackupModelForm(request.POST, instance=obj)
        #     if form.is_valid():
        #         form.save()
        #         logger.info('Datensicherungssatz wurde erfolgreich geändert')
        #         return redirect('administration:backup_list')
        #         context={
        #                 "object":obj,
        #                 "form":form
        #             }
        return render(request, self.template_name, context)




# class cashbox_dashboard_view(ListView):
#     template_name = 'new/cashbox_dashboard_copy.html'
#     queryset = Product.objects.all()



#------------------------------------------



# def cashbox_dashboard_view(request, *args, **kwargs):
#     cardForm = FormCart(request.POST or None)

#     context = {
#         'form': cardForm
#     }
#     return render(request, "cashbox_dashboard.html", context)


# def cashbox_pay_view(request, *args, **kwargs):
#     return render(request, "cashbox_pay.html", {})


# def cashbox_more_view(request, *args, **kwargs):
#     moreForm = FormGetInfo(request.POST or None)

#     context = {
#         'form': moreForm
#     }
#     return render(request, "cashbox_more.html", context)