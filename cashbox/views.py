from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from product.models import Product
from django.http import HttpResponse
from .models import *
from authorization.models import Active_Accounts
from datetime import datetime
from django.db import connection
from collections import namedtuple
from customer.models import Customer
from administration.forms import CustomerModelForm, ReversalBillModelForm



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
        cashboxlist = Cashbox.objects.filter(user=None)

        print("")
        print("GET")




        

        context={

            "cashboxlist":cashboxlist,
            
        }
        return render(request, template_name, context)

    
    # http/POST method
    def post(self, request, id=None, *args, **kwargs):

        # template_name = 'new/cashbox_dashboard_copy.html'
        # template_name = "{% url 'cashbox:cashbox_dashboard' %}"
        
        context={}
        print("")
        print("POST")
        cashboxId = request.POST.get("cashboxId", "")
        print(cashboxId)
        setCashbox(request, cashboxId)
        queryset = Product.objects.all()

        cashbox = getCashbox(request)
        cashbox.user = Active_Accounts.objects.get(user=request.user)
        cashbox.save()

        
        # queryset = Product.objects.all()
        # context={
        #     "object_list":queryset,
        #     "cashbox":cashbox,

        # }
        return redirect('cashbox:cashbox_dashboard')
        # return render(request, template_name, context)


class cashbox_dashboard_view(View):

    template_name = 'new/cashbox_dashboard_copy.html'




    # http/GET method
    def get(self, request, id=None, *args, **kwargs):
        
        context={}
        
        

        produkte = getallproductswithstockzero()
        print(produkte)

        # if 'resetShoppingcart' in request.GET:
        #     print("RESET")
        print("")
        print("GET")
        print(request.method)
        
        request.session['shoppingcartIds'] = []
        print(request.session.get('shoppingcartIds'))

        cashbox = getCashbox(request)



        context={
            "object_list":produkte,
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
        
        
        

        produkte = getallproductswithstockzero()
        context={
            "object_list":produkte,
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

        #total
        total = gettotal(request)

        # queryset = Product.objects.all()
        cashbox = getCashbox(request)


        if paymenttool.title == "Bargeld":

            return redirect('cashbox:cashbox_payment')
        
        

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
        rabatte = Discount.objects.all()

        setdiscount(request, None)
        

        #total
        total = gettotal(request)

        setamountpaid(request, 0.0)
        amountpaid = getamountpaid(request)

        context={
            
            "cashbox":cashbox,
            "total":total, 
            "fehlenderbetrag":total,
            "amountpaid":amountpaid,
            "rabatte":rabatte,
        }
        return render(request, self.template_name, context)

    
    # http/POST method
    def post(self, request, id=None, *args, **kwargs):
  
        context={}
        if 'zahlungabschließen' in request.POST:
            zahlungabschließen(request)
            template_name = 'new/cashbox_dashboard_copy.html'
            
            return redirect('cashbox:cashbox_dashboard')
            

        else:

            
            

            





            # print("++++++")
            # print(request.session.get("discountId", ""))
            # print("++++++")

            # if request.POST.get("discountId", "") is not None:
            #     print("----------")
            #     print("Discount")
            #     print(getdiscount(request))
            #     print("----------")
            # else:
            #     print("----------")
            #     print("Discount")
            #     print("None")
            #     print("----------")

            


    
            print("")
            print("POST")


            
            cashbox = getCashbox(request)
            # queryset = Product.objects.all()

            if 'rabattAuswählen' in request.POST:
                print("In Rabatt Auswählen")
                discountId = request.POST.get("discountId", "")
                setdiscount(request, discountId)

                print(discountId)
            
            if request.session.get("discountId", "") is not None:
                # total mit discount verrechnet
                total = gettotal(request)
                discount = getdiscount(request)
                factor = discount.factor
                rabatt = (total*factor)/100
                total = total - rabatt


                print(factor)
                print("total mit discount verrechnet")
                print(total)
            else:
                # total ohne discount verrechnet
                total = gettotal(request)
                print("total ohne discount verrechnet")
                print(total)


                
            
                       
            

            # rabatte
            rabatte = Discount.objects.all()

            if 'betrag' in request.POST:
                print("Hier in der If Abfrage")
                print(request.POST.get("betrag", ""))
                cashbox = getCashbox(request)
                betrag = request.POST.get("betrag", "")
                cashbox.amount += Decimal(betrag)
                cashbox.save()
                safe = getMinSafe()
                safe.amount -= Decimal(betrag)
                safe.save()
                amountpaid = getamountpaid(request)
                rückzahlung = float(amountpaid)- float(total)
                fehlenderbetrag = float(total) - float(amountpaid)
                minValue = float(rückzahlung) - float(cashbox.amount)
            
            else:

                if 'amountpaid' not in request.session:
                    setamountpaid(request, 0.0)
                    print("NO amountpaid")
                else:
                    amountpaid = getamountpaid(request)

                if 'resetPayment' in request.POST:
                    setamountpaid(request, 0.0)
                    setdiscount(request, None)
                    print("RESET Só")
                
                    
                if 'münze' in request.POST:
                    print("münze")

                    münze = float(request.POST.get("münze", ""))
                    amountpaid += münze
                    setamountpaid(request, amountpaid)

                fehlenderbetrag = float(total) - float(amountpaid)      
                rückzahlung = float(amountpaid)- float(total)
                
                safe = getMinSafe()
                if (float(rückzahlung) - float(cashbox.amount)) > 0:
                    minValue = float(rückzahlung) - float(cashbox.amount)
                else:
                    minValue = 0.0
        
            

        
            context={
                "cashbox":cashbox,
                "total":total,
                "amountpaid":amountpaid,
                "fehlenderbetrag":fehlenderbetrag,
                "rückzahlung":rückzahlung,
                "minValue":minValue,
                "tresor":safe,
                "rabatte":rabatte,
            }

            return render(request, self.template_name, context)
        context={}
        return render(request, self.template_name, context)


class cashbox_reversalbill_view(View):

    template_name = 'new/cashbox_reversalbill_copy.html'
    
    # http/GET method
    def get(self, request, id=None, *args, **kwargs):
        
        context={}
        

        print("")
        print("GET")


        cashbox = getCashbox(request)
        headline = "Lege eine Stornorechnung an"
        
        form = ReversalBillModelForm()
        context={
        
        "cashbox":cashbox,
        "headline":headline,
        "form":form,
        
            
        }
        return render(request, self.template_name, context)

    
    # http/POST method
    def post(self, request, id=None, *args, **kwargs):
       
        context={}
        print("")
        print("POST")

        form = ReversalBillModelForm(request.POST)
        print("sdfsdfsdf")
        print(form.is_valid())
        
        if form.is_valid():
            
            
            form.save()   
            return redirect('cashbox:cashbox_reversalbill')

        cashbox = getCashbox(request)
        
        context={
            "cashbox":cashbox,
            "form":form,
        }
        return render(request, self.template_name, context)


class cashbox_customer_view(View):
    
    # http/GET method
    def get(self, request, id=None, *args, **kwargs):
        template_name = 'new/cashbox_customer_copy.html'
        context={}
        

        print("")
        print("GET")


        cashbox = getCashbox(request)
        kunden = Customer.objects.all()


        context={
            "cashbox":cashbox,
            "object_list":kunden,
        }
        return render(request, template_name, context)

    
    # http/POST method
    def post(self, request, id=None, *args, **kwargs):

        template_name = 'new/cashbox_customer_copy.html'
        
        
        context={}
        print("")
        print("POST")
        

        cashbox = getCashbox(request)
        
        context={
            "cashbox":cashbox,
        }
        return render(request, template_name, context)


class cashbox_customer_create_view(View):
    template_name = 'new/cashbox_customer_createupdate_copy.html'

    # http/GET method
    def get(self, request, *args, **kwargs):
        form = CustomerModelForm()
        headline = "Erstelle deinen Kunden"

        context = {
            "form":form,
            "headline":headline,
        }
        return render(request, self.template_name, context)

    # http/POST method
    def post(self, request, id=None, *args, **kwargs):
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('cashbox:cashbox_customer')
        context = {
            "form":form
        }
        return render(request, self.template_name, context)


class cashbox_customer_update_view(View):
    template_name = 'new/cashbox_customer_createupdate_copy.html'

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
            headline = "Bearbeite einen Kunden"
            context={
                "headline":headline,
                "object":obj,
                "form":form, 
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
                
                return redirect('cashbox:cashbox_customer')
                context={
                        "object":obj,
                        "form":form
                    }
        return render(request, self.template_name, context)

# Methoden

def custom_sql(query):
    with connection.cursor() as cursor:
        cursor.execute(query)
        row = cursor.fetchone()
    return row

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

def getallproductswithstockzero():
    queryset = raw_sql("select p.id AS ID from product_product p left join product_product_category pc on p.id=pc.product_id left join product_category c on pc.category_id=c.id where  p.stock>0 order by c.title;")
    idlist = []
    for i in queryset:
        idlist.append(i.ID)
    print(idlist)

    produkte = getOneDimensionalproductlist(idlist)
    return produkte

def getOneDimensionalproductlist(productIdlist):
    productlist = []

    for id  in productIdlist:
        obj = Product.objects.get(pk=id)
        productlist.append(obj)

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


def getMinSafe():
    query = 'select * from cashbox_safe where amount = (select max(amount) from cashbox_safe);'
    safetupel = raw_sql(query)
    print(safetupel[0].id)
    safe = Safe.objects.get(id=safetupel[0].id)

    return safe


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

def setdiscount(request, id):
    
    request.session['discountId']= id
    

def getdiscount(request):

    if request.session.get("discountId", "") is not None:
        discountId = request.session['discountId']
        discount = Discount.objects.get(id=discountId)
        return discount
    else: 
        return None
   




def zahlungabschließen(request):
    print("Zahlung Abschließen:")


    # create Bill
    
    # employee
    employee = request.user
    print(employee)

    # cashbox
    cashbox = getCashbox(request)
    print(cashbox)

    # paymenttool
    paymenttool = getPaymenttool(request)
    print(paymenttool)

    
    # creation DateTime
    creation = datetime.now()
    print(creation)

    # totalcosts
    if request.session.get("discountId", "") is not None:
        # total mit discount verrechnet
        total = gettotal(request)
        discount = getdiscount(request)
        factor = discount.factor
        rabatt = (total*factor)/100
        total = total - rabatt


        print(factor)
        print("total mit discount verrechnet")
        print(total)
    else:
        # total ohne discount verrechnet
        total = gettotal(request)
        print("total ohne discount verrechnet")
        print(total)
    

    # discount
    discount = getdiscount(request)
    
    # path
    pass

    # sql query

    bill =  Bill.objects.create(cashbox=cashbox, employee=employee, paymenttool=paymenttool, creation=creation , totalcosts=total, discount=discount)

    # create Bill_Product
    idlist = getproductIdlist(request)
    productlist = getproductlist(idlist)

    for product in productlist:
        p = product[0]
        amount = len(product)
        p.stock -= amount
        p.save()
        Bill_Product.objects.create(bill=bill, product=p, amount=amount)

    # Kassengeld wird aktualisiert
    cashbox.amount += Decimal(total)
    cashbox.save()
    


    # Zurück zum Dashboard

    print("ZAHLUNG ABSCHLIESSEN")
    

    

    # produkte = getallproductswithstockzero()
    # print(produkte)

    # # if 'resetShoppingcart' in request.GET:
    # #     print("RESET")
    # print("")
    # print("GET")
    # print(request.method)
    
    # request.session['shoppingcartIds'] = []
    # print(request.session.get('shoppingcartIds'))

    # cashbox = getCashbox(request)
    
    # print("zur Dashboard view")


    # context={
    #     "object_list":produkte,
    #     "cashbox":cashbox,
        
    # }
    # return render(request, template_name, context)
    
    


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