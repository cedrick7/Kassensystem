from django.db import models
from django.utils import timezone
import datetime

from authorization.models import Employee

# Create your models here.


class Worktime(models.Model):
    begin    = models.DateTimeField(blank=True, default=timezone.now)    
    end      = models.DateTimeField(blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, blank=False)


    def duration(self):
        duration = self.begin - self.end
        return duration

    def durationToString(self):
        duration = self.duration()
        return str(int(duration.total_seconds()/3600)) + "h " + str(int(duration.total_seconds()%60)) + "m "


    class Meta:
        verbose_name_plural = "Arbeitszeiten"

    def __str__(self):

        return self.durationToString() + " " + str(self.employee) + " am " + str(self.begin.date())
        # Arbeitszeitduration: Stundenanzahl + Minutenanzahl + Datum + Mitarbeiter 