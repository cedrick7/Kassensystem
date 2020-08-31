from django.db import models

# Create your models here.

class Employee(models.Model):
    firstname       = models.CharField(max_length=45, blank=False)
    lastname        = models.CharField(max_length=45, blank=False)
    username        = models.CharField(max_length=45, blank=False)
    password        = models.CharField(max_length=72, blank=False, editable=True) # default: editable=False
    picture         = models.FileField(upload_to='mit_img/', default='static/mit_img/default.jpg', blank=True)



    CASHIER         = 'KA'
    ADMINISTRATOR   = 'AD'
    ANALYST         = 'AN'
    PERMISSIONS = [
    (CASHIER,     'Kassierer'),
    (ADMINISTRATOR, 'Administrator'),
    (ANALYST,       'Analyst'),
    ]

    role = models.CharField(
        max_length=2,
        choices=PERMISSIONS,
        default=CASHIER,
    )


    def __str__(self):
            return self.getFirstname() + " " + self.getLastname()

    def getFirstname(self):
        return self.firstname

    def getLastname (self):
        return self.lastname

    class Meta:
        verbose_name_plural = "Mitarbeiter"


class Request(models.Model):
    employee     = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, default=None)
    
    PW_RESET   = 'PR'
    AC_CREATE   = 'AC'
    TYPE = [
    (PW_RESET,     'Passwort zurücksetzen'),
    (AC_CREATE, 'Account anlegen'),
    ]

    type = models.CharField(
        max_length=2,
        choices=TYPE,
        blank=False
    )
    firstname       = models.CharField(max_length=45, blank=True)
    lastname        = models.CharField(max_length=45, blank=True)
    password        = models.BinaryField(blank=False, editable=True) # default: editable=False

    CASHIER         = 'KA'
    ADMINISTRATOR   = 'AD'
    ANALYST         = 'AN'
    PERMISSIONS = [
    (CASHIER,     'Kassierer'),
    (ADMINISTRATOR, 'Administrator'),
    (ANALYST,       'Analyst'),
    ]

    role = models.CharField(
        max_length=2,
        choices=PERMISSIONS,
        default=None,
        blank=True
    )

    class Meta:
        verbose_name_plural = "Anfragen"

    def __str__(self):
        return self.firstname + " " + self.lastname + " möchte " + self.type + " " + self.role 