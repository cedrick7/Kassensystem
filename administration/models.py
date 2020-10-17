from django.db import models
from django.utils import timezone
import datetime

from authorization.models import Employee

# Create your models here.



class Path(models.Model):
    store       = models.FileField(upload_to='uploads/')


    class Meta:
        verbose_name_plural = "Paths"



class Backup(models.Model):
    title       = models.CharField(max_length=45)
    creation    = models.DateTimeField(default=timezone.now)
    path       = models.ForeignKey(Path, on_delete=models.CASCADE, blank=True, default=None)
    comment     = models.CharField(max_length=150, blank=True)
    employee     = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, default=None)


    class Meta:
        verbose_name_plural = "Backups"

    def __str__(self):
        return self.title + " from " + self.creation
    
