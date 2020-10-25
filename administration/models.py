from django.db import models
from django.utils import timezone
import datetime
from django.urls import reverse

from django.contrib.auth.models import User

# Create your models here.






class Backup(models.Model):
    title       = models.CharField(max_length=45)
    creation    = models.DateTimeField(default=timezone.now)
    path       = models.FileField(upload_to='uploads/', unique=False)
    comment     = models.CharField(max_length=150, blank=True)
    employee     = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, default=None)


    
    def get_update_url(self):
        return reverse("administration:backup_update", kwargs={"id": self.id})
    
    def get_delete_url(self):
        return reverse("administration:backup_delete", kwargs={"id": self.id})



    class Meta:
        verbose_name_plural = "Backups"

    # def __str__(self):
    #     return self.title + " from " + self.creation
    
