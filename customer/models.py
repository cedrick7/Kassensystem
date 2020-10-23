from django.db import models
from django.urls import reverse

# Create your models here.


# class CustomerDetails(models.Model):
#     phonenumber       = models.DecimalField(max_digits=15, decimal_places=2, blank=True, unique=True)
#     email             = models.EmailField(max_length=254)
    

class Customer(models.Model):
    firstname         = models.CharField(max_length=45, blank=True)
    lastname          = models.CharField(max_length=45, blank=True)
    birthday           = models.DateField(max_length=45,default=None, )
    # details       = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE, blank=True, default=None)
    phonenumber       = models.DecimalField(max_digits=15, decimal_places=0, blank=True, unique=True)
    email             = models.EmailField(max_length=254, blank=True, unique=True)

    def get_update_url(self):
        return reverse("administration:customer_update", kwargs={"id": self.id})
    
    def get_delete_url(self):
        return reverse("administration:customer_delete", kwargs={"id": self.id})


    class Meta:
        verbose_name_plural = "Customern"

    def __str__(self):
        return self.firstname + " " + self.lastname