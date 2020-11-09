from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from product.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from authorization.models import Active_Accounts
from datetime import datetime
from django.db import connection
from collections import namedtuple
from customer.models import Customer
from administration.forms import CustomerModelForm, ReversalBillModelForm, Bill_ProductModelForm
import math

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
                safe = getMaxSafe()
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
                
                safe = getMaxSafe()
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
        headline = "Für welche Rechnung eine Stornorechnung erstellen"
        
        # der User sieht nur Rechnungen, die er selber erstellt hat 
        objectlist = Bill.objects.filter(isReversalbill=False, employee=request.user)
        

        context={
        
        "cashbox":cashbox,
        "headline":headline,
        "object_list":objectlist,
        
            
        }
        return render(request, self.template_name, context)

    
    # http/POST method
    def post(self, request, id=None, *args, **kwargs):
        context = {}
        billId = request.POST.get('billId')
        print("hier ist get")
        print(billId)

        # Stornorechnung wird angelegt
        original = Bill.objects.get(id=billId)
        new = Bill.objects.create(creation=datetime.now(), totalcosts=original.totalcosts, cashbox=original.cashbox, discount=original.discount, employee=original.employee, paymenttool=original.paymenttool, isReversalbill=True, linkedbill=original)
        new.save()

        # Bill_Product hinzufügen
        queryset = Bill_Product.objects.filter(bill=original.id)
        for i in queryset:
            obj = Bill_Product.objects.create(bill=new, product=i.product, amount=i.amount)
            obj.save()
        


        return HttpResponseRedirect(reverse("cashbox:cashbox_bill_change", kwargs={"id": new.id}))



class Bill_ProductListView(View):
   

    template_name = 'new/cashbox_change_bill_list_copy.html'

    # http/GET method
    def get(self, request, id=None, *args, **kwargs):

        new = Bill.objects.get(id=id)
        
        id = new.id
        objs = Bill_Product.objects.filter(bill=new)
        

        # if id is not None:
        #     obj = get_object_or_404(Bill, id=id)
        #     billproductIdlist = Bill_Product.objects.filter(bill=id).values_list('product', 'amount')
        #     print(billproductIdlist)
        #     productlist = []

        #     for i in billproductIdlist:
        #         p = Product.objects.get(id=i[0])
        #         amount = i[1]
                
        #         for x in range(amount):

        #             productlist.append(p)

        context = {
            "id":id,
            "objectlist":objs,    
        }
            
        return render(request, self.template_name, context)


    # http/POST method
    def post(self, request, id=None, *args, **kwargs):
        print("Hier in Post")

        if 'Ändern' in request.POST:
            print("Hier in Ändern")

            pid=0
            pid = request.POST.get("productId")
            print(id)
            obj = Bill_Product.objects.filter(bill=id, product=pid)
            print(obj[0].bill.id)

            return HttpResponseRedirect(reverse("cashbox:cashbox_bill_detail_change", kwargs={"id": obj[0].bill.id, "pid": obj[0].product.id}))

        

        if 'Abbrechen' in request.POST:
            print("in If Abfrage")
            reversalbillId = request.POST['billId']
            reversalbill = Bill.objects.get(id=reversalbillId)
            Bill_Product.objects.filter(bill=reversalbill).delete()
            Bill.objects.get(id=reversalbillId).delete()
            return redirect("cashbox:cashbox_reversalbill")

        if 'Abschließen' in request.POST:
            print("Hier in Abschließen")

            # totalcosts aktualisieren
            bill = Bill.objects.get(id=id)
            
            newtotal = calctotalfromBill(bill)

            bill.totalcosts = newtotal
            


            # refund ausrechnen
            oldtotal = bill.linkedbill.totalcosts

            refund = float(oldtotal) - newtotal
            
            # Kassengeld wird aktualisiert
            einzahlung = 0
            if refund>0: # wegen rechnen-Schwierigkeiten
                
                if refund>getCashbox(request).amount: # zu wenig Geld in der Kasse
                    safe = getMaxSafe()
                    cashbox = getCashbox(request)
                    roundednum = roundup(refund)
                    einzahlung = roundednum
                    safe.amount-= Decimal(roundednum) # Geld wird aus Safe gezogen
                    safe.save()
                    cashbox.amount+= Decimal(roundednum) # Geld wird in Kasse eingezahlt
                
                cashbox = getCashbox(request) # Kassengeld wird aktualisiert
                cashbox.amount-= Decimal(refund)

            # Bestände werden aktualisiert
            originalbill = bill.linkedbill
            originalproductlist = []
            originalqueryset = Bill_Product.objects.filter(bill=originalbill)
            for i in originalqueryset:
                originalproductlist.append(i)

            print(originalproductlist)
            
            newproductlist = []
            newqueryset = Bill_Product.objects.filter(bill=bill)
            for i in newqueryset:
                newproductlist.append(i)

            if len(originalproductlist) == len(newproductlist):
                length = len(newproductlist)
                for i in range(length):
                    if originalproductlist[i].product == newproductlist[i].product:
                        oldamount = originalproductlist[i].amount
                        newamount = newproductlist[i].amount
                        korrektur = oldamount - newamount
                        if 0<korrektur:
                            originalproductlist[i].product.stock += korrektur # Bestand wird aktualisiert
                            
                            bill.refund = refund
                            
                            # Alles speichern
                            bill.save()
                            cashbox.save()
                            cashbox.save()
                            originalproductlist[i].product.save()

                            # Weiterleitung
                            request.session['refund'] = refund
                            request.session['einzahlung'] = einzahlung
                            
                            return redirect('cashbox:cashbox_reversalbill_success')
                            
                                                    

                        elif korrektur<0:
                            print("Möchten Sie Waren dazu rechnen, erstellen Sie bitte eine neue Rechnung.")
                            print("Korrigieren Sie bitte die richtige Anzahl.")
                    else: 
                        print("Etwas ist mit den Beständen schief gelaufen")
            

            # Zurück zum Warenkorb

            return redirect("cashbox:cashbox_dashboard")
                





  
class Bill_ProductDetailView(View):
    template_name = 'new/cashbox_bill_detail_copy.html'

    # http/GET method
    def get(self, request, id=None, pid=None, *args, **kwargs):
        context = {}
        print("Hier in Get")
        print(id)
        print(pid)

    
        queryset = Bill_Product.objects.filter(bill=id, product=pid)
        obj = queryset[0]
        print(obj)
        if obj is not None:
            form = Bill_ProductModelForm(instance=obj)
            context={
                "obj":obj,
                "form":form, 
                
            }
        return render(request, self.template_name, context)


    # http/POST method
    def post(self, request, id=None, *args, **kwargs):
        print("Hier in Post:")
        print(id)
        pid = request.POST.get('productId')
        print(pid)
        bill = Bill.objects.get(id=id)
        product = Product.objects.get(id=pid)
        obj = Bill_Product.objects.get(bill=bill, product=product)
        print(obj)
        if obj is not None:
            form = Bill_ProductModelForm(request.POST, instance=obj)
            if form.is_valid():
                print("form is valid")
                form.save()
                
        return HttpResponseRedirect(reverse("cashbox:cashbox_bill_change", kwargs={"id": id}))

class ReversalBillSuccess(View):
    template_name = 'new/cashbox_reversalbill_success.html'

    def get(self, request, id=None, *args, **kwargs):
        context = {}
        print("Hier in Get")

        refund = 0.0
        einzahlung = 0.0
        
        refund = request.session.get('refund')
        einzahlung = request.session.get('einzahlung')

        
        context={
            "refund":refund, 
            "einzahlung":einzahlung,             
            
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

def calctotalfromBill(bill):
    total = 0.0
    
    id = bill.id
    query = "select bp.amount, p.costs from cashbox_bill_product bp join product_product p on (bp.product_id=p.id) where bp.bill_id="+str(id)+";"
    result = raw_sql(query)

    for i in result:
        total += float(Decimal(i[0])*Decimal(i[1]))
     
    # Discount
    if bill.discount is not None:
        factor = bill.discount.factor
        rabatt = (total*float(factor))/100
        total = total - rabatt
    
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


def getMaxSafe():
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
   

def roundup(x):
    return int(math.ceil(x / 10.0)) * 10



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