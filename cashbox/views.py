from django.shortcuts import render
from .forms import *
from product.models import Product
from django.http import HttpResponse
from .models import *
from datetime import datetime
from django.db import connection
from collections import namedtuple


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


# Class Based Views

class choose_cashbox_view(View):
    

    # http/GET method
    def get(self, request, id=None, *args, **kwargs):
        template_name = 'new/choose_cashbox_copy.html'
        context={}
        cashboxlist = Cashbox.objects.all()

        print("")
        print("GET")




        

        context={

            "cashboxlist":cashboxlist,
            
        }
        return render(request, template_name, context)

    
    # http/POST method
    def post(self, request, id=None, *args, **kwargs):

        template_name = 'new/cashbox_dashboard_copy.html'
        # template_name = "{% url 'cashbox:cashbox_dashboard' %}"
        
        context={}
        print("")
        print("POST")
        cashboxId = request.POST.get("cashboxId", "")
        print(cashboxId)
        setCashbox(request, cashboxId)
        queryset = Product.objects.all()
        cashbox = getCashbox(request)

        
        # queryset = Product.objects.all()
        context={
            "object_list":queryset,
            "cashbox":cashbox,

        }
        return render(request, template_name, context)


class cashbox_dashboard_view(View):

    template_name = 'new/cashbox_dashboard_copy.html'




    # http/GET method
    def get(self, request, id=None, *args, **kwargs):
        
        context={}
        queryset = Product.objects.all()
        # if 'resetShoppingcart' in request.GET:
        #     print("RESET")
        print("")
        print("GET")
        print(request.method)
        
        request.session['shoppingcartIds'] = []
        print(request.session.get('shoppingcartIds'))

        cashbox = getCashbox(request)



        context={
            "object_list":queryset,
            "cashbox":cashbox,
            
        }
        return render(request, self.template_name, context)

    
    # http/POST method
    def post(self, request, id=None, *args, **kwargs):
        
        
        context={}
        cashbox = getCashbox(request)
        productId = request.POST.get("productId", "")
        
        
        productIdlist = request.session['shoppingcartIds']
        
        productIdlist.append(productId)

        request.session['shoppingcartIds'] = productIdlist



        
        print("")
        print("POST")


        #total
        total = gettotal(request)


        #productlist 
        productIdlist = getproductIdlist(request)
        productlist = getproductlist(productIdlist)
        
        
        

        queryset = Product.objects.all()
        context={
            "object_list":queryset,
            "shoppingcart":productlist,
            "totalcosts":total,
            "cashbox":cashbox,
        }

        return render(request, self.template_name, context)


class choose_paymenttool_view(View):
    

    # http/GET method
    def get(self, request, id=None, *args, **kwargs):
        template_name = 'new/cashbox_choose_paymenttool_copy.html'
        context={}


        print("")
        print("GET")

        paymenttoollist = Paymenttool.objects.all()


        context={

            "paymenttoollist":paymenttoollist,
            
        }
        return render(request, template_name, context)

    
    # http/POST method
    def post(self, request, id=None, *args, **kwargs):

        template_name = 'new/cashbox_choose_paymenttool_copy.html'
        
        context={}
        print("")
        print("POST")
        paymenttoollist = Paymenttool.objects.all()
        paymenttoolId = request.POST.get("paymenttoolId", "")
        
        setPaymenttool(request, paymenttoolId)
        paymenttool = getPaymenttool(request)

        if paymenttool.title == "Bargeld":

            template_name = 'new/cashbox_pay_copy.html'
        
        #total
        total = gettotal(request)



        
        # queryset = Product.objects.all()
        cashbox = getCashbox(request)

        context={
            "paymenttoollist":paymenttoollist,
            "cashbox":cashbox,
            "total":total
            
        }
        return render(request, template_name, context)


class cashbox_payment_view(View):
    template_name = 'new/cashbox_pay_copy.html'

     # http/GET method
    def get(self, request, id=None, *args, **kwargs):
        
        context={}
        
        # queryset = Product.objects.all()

        print("")
        print("GET")
          
        cashbox = getCashbox(request)
        

        #total
        total = gettotal(request)

        amountpaid = getamountpaid(request)

        context={
            
            "cashbox":cashbox,
            "total":total, 
            "amountpaid":amountpaid,
        }
        return render(request, self.template_name, context)

    
    # http/POST method
    def post(self, request, id=None, *args, **kwargs):
  
        context={}
        if 'zahlungabschließen' in request.POST:
            zahlungabschließen(request)


        else:

    
            print("")
            print("POST")
            
            cashbox = getCashbox(request)
            # queryset = Product.objects.all()
            
            #total
            total = gettotal(request)
           
            
            if 'amountpaid' not in request.session:
                setamountpaid(request, 0.0)
                print("NO amountpaid")
            else:
                amountpaid = getamountpaid(request)

            if 'resetPayment' in request.POST:
                setamountpaid(request, 0.0)
                
                print("RESET Só")
            else:
                münze = float(request.POST.get("münze", ""))
                amountpaid += münze
                setamountpaid(request, amountpaid)

            fehlenderbetrag = float(total) - float(amountpaid)      
            rückzahlung = float(amountpaid)- float(total)
        
    	
        
            context={
                "cashbox":cashbox,
                "total":total,
                "amountpaid":amountpaid,
                "fehlenderbetrag":fehlenderbetrag,
                "rückzahlung":rückzahlung,
            }

            return render(request, self.template_name, context)
        context={}
        return render(request, self.template_name, context)


# Methoden

def getproductIdlist(request):
    productIdlist = request.session['shoppingcartIds'] 
    return productIdlist

def getproductlist(productIdlist):
    productIdlist.sort()
    productlist = []
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

    return productlist


def calctotal(productlist):
    
    
    total = 0

    for list in productlist:
        for p in list:
            total += p.costs
        
    return total

def gettotal(request):
    productIdlist = getproductIdlist(request)
    total = 0.0
    productlist = getproductlist(productIdlist)
    total = calctotal(productlist)
    return total



def takeoutProduct(request, *args, **kwargs):
    print("SKRRRR")
    print(request)
    template_name = 'new/cashbox_dashboard_copy.html'

    #total
    total = gettotal(request)



    cashbox = getCashbox(request)
    queryset = Product.objects.all()
    context={
        "object_list":queryset,
        "shoppingcart":productlist,
        "totalcosts":total,
        "cashbox":cashbox,
    }

    return render(request, template_name, context)


def setCashbox(request, cashboxId):
    request.session['cashboxId'] = cashboxId

def getCashbox(request):
    if 'cashboxId' in request.session:
        id = request.session.get('cashboxId')
        cashbox = Cashbox.objects.get(pk=id)
        return cashbox
    else:
        return None

def getCashboxId(request):

    if 'cashboxId' in request.session:
        id = request.session.get('cashboxId')
        return id
    else:
        return None


def setPaymenttool(request, paymenttoolId):
    request.session['paymenttoolId'] = paymenttoolId

def getPaymenttool(request):
    if 'paymenttoolId' in request.session:
        id = request.session.get('paymenttoolId')
        paymenttool = Paymenttool.objects.get(pk=id)
        return paymenttool
    else:
        return None

def getPaymenttoolId(request):
    if 'paymenttoolId' in request.session:
        id = request.session.get('paymenttoolId')
        return id
    else:
        return None


def setamountpaid(request, value):
    
    request.session['amountpaid']= float(value)
    print(value)

def getamountpaid(request):

    if 'amountpaid' in request.session:
        amountpaid = request.session['amountpaid']
        print("AMOUNTPAID")
        return amountpaid
    else: 
        return 0.0


def zahlungabschließen(request):
    print("Zahlung Abschließen:")

    # create Bill
    
    # employee
    employeefk = request.user.id 
    print(employeefk)

    # cashbox
    cashboxfk = getCashboxId(request)
    print(cashboxfk)

    # paymenttool
    paymenttoolfk = getPaymenttoolId(request)
    print(paymenttoolfk)

    
    # creation DateTime
    creation = datetime.now()
    print(creation)

    # totalcosts
    total=gettotal(request)
    print(total)

    # discount
    pass
    
    # path
    pass

    # sql query
    query = "INSERT INTO 07yp3juew2.cashbox_bill (cashbox, employee, paymenttool, creation, totalcosts) VALUES (cashboxfk, employeefk, paymenttoolfk, total);"
    print(raw_sql(query))      
    # create Bill_Product

    # get rechnung id by creation



# RawSQL
def raw_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        desc = cursor.description
        nt_result = namedtuple('Result', [col[0] for col in desc])
        return [nt_result(*row) for row in cursor.fetchall()]


# if 'amountpaid' not in request.session:

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