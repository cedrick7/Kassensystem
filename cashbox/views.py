from django.shortcuts import render
from .forms import *
from product.models import Product
from django.http import HttpResponse


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


class cashbox_payment_view(View):
    template_name = 'new/cashbox_pay_copy.html'
     # http/GET method
    def get(self, request, id=None, *args, **kwargs):
        
        context={}
        
        # queryset = Product.objects.all()

        print("")
        print("GET")
  

        context={
            
            
        }
        return render(request, self.template_name, context)

    
    # http/POST method
    def post(self, request, id=None, *args, **kwargs):
  
        context={}
 
        print("")
        print("POST")
        

        # queryset = Product.objects.all()
        context={


        }
        return render(request, self.template_name, context)


class cashbox_dashboard_view(View):

    template_name = 'new/cashbox_dashboard_copy.html'




    # http/GET method
    def get(self, request, id=None, *args, **kwargs):
        
        context={}
        queryset = Product.objects.all()

        print("")
        print("GET")
        print(request.method)
        
        request.session['shoppingcartIds'] = []
        print(request.session.get('shoppingcartIds'))




        

        context={
            "object_list":queryset,
            
        }
        return render(request, self.template_name, context)

    
    # http/POST method
    def post(self, request, id=None, *args, **kwargs):

        
        context={}

        productId = request.POST.get("productId", "")
        
        
        productIdlist = request.session['shoppingcartIds']
        
        productIdlist.append(productId)

        request.session['shoppingcartIds'] = productIdlist



        
        print("")
        print("POST")
        print(request.session.get('shoppingcartIds'))
        
        productlist = []
        
        
        productIdlist.sort()
        print(productIdlist)
 
        include = False
        for id in productIdlist:
            obj = Product.objects.get(pk=id)

            for list in productlist:

                if obj in list:
                    print("True")
                    include = True
                    list.append(obj)

            if include is False:
                productlist.append([obj])
            else: 
                include = False

        print("Produktliste Davor:")
        print(productlist)

        # if 'delete' in request.POST:
        #     print("DELETE")
        #     print(request.POST.get("productId", ""))

        print("Produktliste Danach:")
        print(productlist)

        total = 0

        for list in productlist:
            for p in list:
                total += p.costs
        

        queryset = Product.objects.all()
        context={
            "object_list":queryset,
            "shoppingcart":productlist,
            "totalcosts":total

        }
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