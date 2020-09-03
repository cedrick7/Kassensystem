from django.db import models

from django.utils import timezone


# Create your models here.


class Property(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "propertyen"

    def __str__(self):
        
        return self.title



class Discount(models.Model):
    title           = models.CharField(max_length=45, null=True)
    factor          = models.DecimalField(max_digits=3,decimal_places=0, default=0) # max: 3 Stellen
    amount          = models.IntegerField(default=0, blank=True)
    begin       = models.DateTimeField(blank=True, default=timezone.now)    # wenn blank, dann permanent 
    end         = models.DateTimeField(blank=True, null=True)


    class Meta:
        verbose_name_plural = "discounte"

    def __str__(self):
        return self.title + str(self.factor) + "% "



class Category(models.Model):
    title       = models.CharField(max_length=45)
    discount      = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, default=None, null=True)

    class Meta:
        verbose_name_plural = "categorien"

    def __str__(self):
        return self.title


class Tax(models.Model):
    taxrate      = models.DecimalField(max_digits=2,decimal_places=0, blank=True, null=True)

    class Meta:
        verbose_name_plural = "taxsätze"

    def __str__(self):

        return "taxrate: "+ self.taxrate + "%"

class Product(models.Model):
    title        = models.CharField(max_length=45)
    category    = models.ManyToManyField(Category, blank=True)
    #description =    Model for Description
    costs       = models.DecimalField(max_digits=4,decimal_places=2)
    weight      = models.DecimalField(max_digits=6,decimal_places=0, null=True, blank=True) # in Gramm
    stock      = models.IntegerField
    brand        = models.CharField(max_length=45, blank=True)
    tax       = models.ForeignKey(Tax, on_delete=models.CASCADE, blank=True, default=None, null=True)
    discount       = models.ForeignKey(Discount, on_delete=models.CASCADE, blank=True, default=None, null=True)
    picture         = models.FileField(upload_to='pro_img/', default='mit_img/default.jpg', blank=True)
    property  = models.ManyToManyField(Property, blank=True)
    #color = Model for colorfield
    #is_favourite = Model for Boolean checkbox
    Service   = 'DI'
    PRODUCT   = 'PR'
    TYPE = [
    (Service, 'Dienstleistung'),
    (PRODUCT, 'Product'),
    ]

    type = models.CharField(
        max_length=2,
        choices=TYPE,
        default=PRODUCT,
    )

    
    class Meta:
        verbose_name_plural = "Producte"

    # prints brand + ProduCttitle, wenn brand leer Nur ProduCttitle
    def __str__(self):
        
        if(self.brand == ""):
            return self.title
        else:
            return self.brand + " "+ self.title
