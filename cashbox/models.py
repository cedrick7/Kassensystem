from django.db import models
from django.contrib.auth.models import User
from product.models import Discount      #cannot import
from product.models import Product
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.urls import reverse
from authorization.models import Active_Accounts

# Create your models here.


class Cashbox(models.Model):
    title       = models.CharField(max_length=45)
    amount      = models.DecimalField(max_digits=6,decimal_places=2, validators=[MinValueValidator(Decimal('-0.01'))]) # in Euro
    user        = models.OneToOneField(Active_Accounts, on_delete=models.CASCADE, null=True)
    
    def get_update_url(self):
        return reverse("administration:cashbox_update", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("administration:cashbox_delete", kwargs={"id": self.id})


    class Meta:
        verbose_name_plural = "Cashboxn"

    def __str__(self):
        return self.title


class Paymenttool(models.Model):
    title        = models.CharField(max_length=45)
    path       = models.FileField(upload_to='uploads/', blank=True, default=None, null=True, unique=False)

    def get_update_url(self):
        return reverse("administration:paymenttool_update", kwargs={"id": self.id})
    
    def get_delete_url(self):
        return reverse("administration:paymenttool_delete", kwargs={"id": self.id})

    class Meta:
        verbose_name_plural = "paymenttool"

    def __str__(self):
        return self.title

class Safe(models.Model):
    title       = models.CharField(max_length=45)
    amount      = models.DecimalField(max_digits=8,decimal_places=2, validators=[MinValueValidator(Decimal('-0.01'))]) # in Euro
    employee = models.ManyToManyField(User, blank=True)

    def get_update_url(self):
        return reverse("administration:safe_update", kwargs={"id": self.id})
    
    def get_delete_url(self):
        return reverse("administration:safe_delete", kwargs={"id": self.id})



    class Meta:
        verbose_name_plural = "Tresore"

    def __str__(self):
        return self.title


class Bill(models.Model):
    creation        = models.DateTimeField(blank=False)
    totalcosts    = models.DecimalField(max_digits=7,decimal_places=2, blank=True, default=0) # max: 10.000,00 # in Euro
    # productamount   = models.IntegerField(default=0) Wird zur Laufzeit ausgerechnet
    employee     = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    cashbox           = models.ForeignKey(Cashbox, on_delete=models.CASCADE, blank=False)
    paymenttool  = models.ForeignKey(Paymenttool, on_delete=models.CASCADE, default=None)
    discount          = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, default=None, null=True) # in Prozent
    path       = models.FileField(upload_to='uploads/', unique=False, blank=True)
    linkedbill = models.ForeignKey("Bill", on_delete=models.CASCADE, blank=True, null=True)
    isReversalbill = models.BooleanField(default=False)
    refund = models.DecimalField(blank=True, default=0, max_digits=8,decimal_places=2)
    

    def get_detail_url(self):
        return reverse("administration:bill_details", kwargs={"id": self.id})
    
    def get_reversal_detail_url(self):
        return reverse("administration:reversalbill_details", kwargs={"id": self.id})

    
    def change_url(self):
        return reverse("cashbox:cashbox_bill_change", kwargs={"id": self.id})

    

    class Meta:
        verbose_name_plural = "Rechnungen"

    def __str__(self):
        return "Rechnung vom "+ str(self.creation.date()) +" von " + str(self.employee)


class Bill_Product(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False)
    amount = models.IntegerField(default=50, validators=[MinValueValidator(Decimal('-0.01'))]) # in Stück


    class Meta:
        unique_together=[['bill', 'product']]


    # Video: https://www.youtube.com/watch?v=-HuTlmEVOgU



class ReversalBill(models.Model):
    creation        = models.DateTimeField(blank=False)
    refund  = models.DecimalField(max_digits=7,decimal_places=2, blank=True, default=0) # max: 99.999,99, Negativ-Werte abfangen
    # productamount   = models.IntegerField(default=0) Wird zur Laufzeit ausgerechnet
    employee     = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    cashbox           = models.ForeignKey(Cashbox, on_delete=models.CASCADE, blank=False)
    path       = models.FileField(upload_to='uploads/', unique=False, blank=True)
    bill        = models.ForeignKey(Bill, on_delete=models.CASCADE, blank=False)
    
    def get_detail_url(self):
        return reverse("administration:reversalbill_details", kwargs={"id": self.id})
    

    class Meta:
        verbose_name_plural = "Stornorechnungen"

    def __str__(self):
        return "Stornorechnung vom "+ str(self.creation.date())