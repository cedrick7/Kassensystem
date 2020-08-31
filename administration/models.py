from django.db import models
from django.utils import timezone
import datetime

from authorization.models import Employee

# Create your models here.


class Backup(models.Model):
    title       = models.CharField(max_length=45)
    creation    = models.DateTimeField(default=timezone.now)
    store       = models.FileField(upload_to='uploads/')
    comment     = models.CharField(max_length=150, blank=True)
    employee     = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=True, default=None)

    class Meta:
        verbose_name_plural = "Backups"

    def __str__(self):
        return self.title + " from " + self.creation

