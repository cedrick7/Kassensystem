from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

# Mitarbeiter
# class Employee(models.Model):
#     # geändert und hinzugefügt
#     firstname            = models.CharField(max_length=45, blank=False)
#     lastname             = models.CharField(max_length=45, blank=False)
#     password             = models.CharField(max_length=73, blank=False, editable=True)
#     picture              = models.FileField(upload_to='mit_img/', default='static/mit_img/default.jpg', blank=True)

#     # ROLE_CHOICE = [
#     #    ('cashier', 'Kassierer'),
#     #    ('admin', 'Administrator'),
#     #    ('analyst', 'Analyst')]
#     # role_select          = models.CharField(max_length= 25, blank=False, null=True, choices = role_choice)


#     CASHIER         = 'KA'
#     ADMINISTRATOR   = 'AD'
#     ANALYST         = 'AN'
#     PERMISSIONS = [
#     (CASHIER,     'Kassierer'),
#     (ADMINISTRATOR, 'Administrator'),
#     (ANALYST,       'Analyst'),
#     ]

#     role = models.CharField(
#         max_length=2,
#         choices=PERMISSIONS,
#         default=CASHIER,
#     )


#     def get_update_url(self):
#         return reverse("administration:employee_update", kwargs={"id": self.id})
    
#     def get_delete_url(self):
#         return reverse("administration:employee_delete", kwargs={"id": self.id})


#     def __str__(self):
#             return self.getFirstname() + " " + self.getLastname()

#     def getFirstname(self):
#         return self.firstname

#     def getLastname (self):
#         return self.lastname

#     class Meta:
#         verbose_name_plural = "Mitarbeiter"

# class Employee(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
    
#     CASHIER         = 'KA'
#     ADMINISTRATOR   = 'AD'
#     ANALYST         = 'AN'
#     PERMISSIONS = [
#     (CASHIER,     'Kassierer'),
#     (ADMINISTRATOR, 'Administrator'),
#     (ANALYST,       'Analyst'),
#     ]

#     role = models.CharField(
#         max_length=2,
#         choices=PERMISSIONS,
#         default=CASHIER,
#     )



# Anfragen
class Request(models.Model):
    PW_RESET   = 'PR'
    AC_CREATE   = 'AC'
    TYPE = [
    (PW_RESET,  'Passwort zurücksetzen'),
    (AC_CREATE, 'Account anlegen'),
    ]

    firstname            = models.CharField(max_length=150, blank=True) 
    lastname             = models.CharField(max_length=150, blank=True) 
    username             = models.CharField(max_length=150, blank=True) 
    admin                = models.BooleanField(default=False)
    analyst              = models.BooleanField(default=False)
    kassierer            = models.BooleanField(default=False)

    type = models.CharField(
        max_length=2,
        choices=TYPE,
        default=AC_CREATE
    )

    def get_delete_url(self):
        return reverse("authorization:delete", kwargs={"username": self.username, "type":self.type})

    def get_accept_url(self):
        return reverse("authorization:accept", kwargs={"username": self.username, "type":self.type})

class Active_Accounts(models.Model):
    username = models.CharField(max_length=150, blank=True) 

































# class Request(models.Model):
#     employee     = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=None)
    
#     PW_RESET   = 'PR'
#     AC_CREATE   = 'AC'
#     TYPE = [
#     (PW_RESET,     'Passwort zurücksetzen'),
#     (AC_CREATE, 'Account anlegen'),
#     ]

#     type = models.CharField(
#         max_length=2,
#         choices=TYPE,
#         blank=False
#     )
#     firstname       = models.CharField(max_length=45, blank=True)
#     lastname        = models.CharField(max_length=45, blank=True)
#     password        = models.CharField(max_length=73, blank=False, editable=True) # default: editable=False

#     CASHIER         = 'KA'
#     ADMINISTRATOR   = 'AD'
#     ANALYST         = 'AN'
#     PERMISSIONS = [
#     (CASHIER,     'Kassierer'),
#     (ADMINISTRATOR, 'Administrator'),
#     (ANALYST,       'Analyst'),
#     ]

#     role = models.CharField(
#         max_length=2,
#         choices=PERMISSIONS,
#         default=None,
#         blank=True
#     )

#     requestid       = models.CharField(max_length=10, unique=True)

#     class Meta:
#         verbose_name_plural = "Anfragen"

#     def __str__(self):
#         return self.firstname + " " + self.lastname + " möchte " + self.type + " " + self.role 


