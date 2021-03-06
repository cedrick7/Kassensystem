from django.db import models
from colorfield.fields import ColorField
from django.utils import timezone
from decimal import Decimal
from django.core.validators import MinValueValidator
from django.urls import reverse



# Create your models here.


class Attribute(models.Model): 
    title = models.CharField(max_length=30)


    def get_update_url(self):
        return reverse("administration:attribute_update", kwargs={"id": self.id})
    
    def get_delete_url(self):
        return reverse("administration:attribute_delete", kwargs={"id": self.id})


    class Meta:
        verbose_name_plural = "attributes"

    def __str__(self):
        
        return self.title



class Discount(models.Model):
    title       = models.CharField(max_length=45, null=True)
    factor      = models.DecimalField(max_digits=3,decimal_places=0, default=0) # max: 3 Stellen # in Prozent
    amount      = models.IntegerField(default=0, blank=True, validators=[MinValueValidator(Decimal('-0.01'))]) # in Stück
    begin       = models.DateTimeField(blank=True, default=timezone.now)    # wenn blank, dann permanent 
    end         = models.DateTimeField(blank=True, null=True)


    def get_update_url(self):
        return reverse("administration:discount_update", kwargs={"id": self.id})
    
    def get_delete_url(self):
        return reverse("administration:discount_delete", kwargs={"id": self.id})


    class Meta:
        verbose_name_plural = "discounte"

    def __str__(self):
        return self.title + str(self.factor) + "% "



class Category(models.Model):
    title       =   models.CharField(max_length=45)
    discount    =   models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, default=None, null=True) # in Prozent
    color       =   ColorField(default='#FF0000')
        
    def get_update_url(self):
        return reverse("administration:category_update", kwargs={"id": self.id})
    
    def get_delete_url(self):
        return reverse("administration:category_delete", kwargs={"id": self.id})


    class Meta:
        verbose_name_plural = "categorien"

    def __str__(self):
        return self.title


class Tax(models.Model):
    title       = models.CharField(max_length=45, null=True)
    taxrate      = models.DecimalField(max_digits=2,decimal_places=0, blank=True, null=True, validators=[MinValueValidator(Decimal('-0.01'))])  # in Prozent


    def get_update_url(self):
        return reverse("administration:tax_update", kwargs={"id": self.id})
    
    def get_delete_url(self):
        return reverse("administration:tax_delete", kwargs={"id": self.id})


    class Meta:
        verbose_name_plural = "taxsätze"



class Product(models.Model):
    title        =  models.CharField(max_length=45)
    category    =   models.ManyToManyField(Category, blank=True)
    description =   models.CharField(max_length=255, blank=True)
    costs       =   models.DecimalField(max_digits=8,decimal_places=2, validators=[MinValueValidator(Decimal('-0.01'))])   # in Euro
    weight      =   models.DecimalField(max_digits=8,decimal_places=0, null=True, blank=True, validators=[MinValueValidator(Decimal('-0.01'))]) # in Gramm
    stock      =    models.IntegerField(blank=True, validators=[MinValueValidator(Decimal('-0.01'))]) # in Stück
    brand        =  models.CharField(max_length=45, blank=True)
    tax       =     models.ForeignKey(Tax, on_delete=models.CASCADE, blank=True, default=None, null=True) # in Prozent
    discount      = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, default=None, null=True) # in Prozent
    path    = models.FileField(upload_to='uploads/', blank=True, default=None, null=True)
    attributes  =   models.ManyToManyField(Attribute, blank=True)
    #color = Model for colorfield
    #is_favourite = Model for Boolean checkbox
    Service   = 'DI'
    PRODUCT   = 'PR'
    TYPE = [
    (Service, 'Dienstleistung'),
    (PRODUCT, 'Produkt'),
    ]

    type = models.CharField(
        max_length=2,
        choices=TYPE,
        default=PRODUCT,
    )

    
    def get_update_url(self):
        return reverse("administration:product_update", kwargs={"id": self.id})
    
    def get_delete_url(self):
        return reverse("administration:product_delete", kwargs={"id": self.id})



    class Meta:
        verbose_name_plural = "Products"
        ordering = ['type']



    # prints brand + Producttitle, wenn brand leer Nur ProduCttitle
    def __str__(self):
        
        if(self.brand == ""):
            return self.title
        else:
            return self.brand + " "+ self.title
