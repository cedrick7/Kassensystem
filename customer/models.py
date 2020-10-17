from django.db import models

# Create your models here.


class CustomerDetails(models.Model):
    phonenumber       = models.DecimalField(max_digits=45, decimal_places=2, blank=True, unique=True)
    email             = models.EmailField(max_length=254)
    

class Customer(models.Model):
    firstname         = models.CharField(max_length=45, blank=True)
    lastname          = models.CharField(max_length=45, blank=True)
    birthday           = models.DateField(max_length=45)
    details       = models.ForeignKey(CustomerDetails, on_delete=models.CASCADE, blank=True, default=None)

    class Meta:
        verbose_name_plural = "Customern"

    def __str__(self):
        return self.firstname + " " + self.lastname