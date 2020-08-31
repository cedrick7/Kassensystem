from django.db import models

# Create your models here.


class Customer(models.Model):
    firstname         = models.CharField(max_length=45, blank=True)
    lastname          = models.CharField(max_length=45, blank=True)
    phonenumber       = models.CharField(max_length=45, blank=True, unique=True)
    notes           = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Customern"

    def __str__(self):
        return self.firstname + " " + self.lastname