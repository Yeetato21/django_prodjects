from django.db import models
import datetime

# Create your models here.


class TimeSlot(models.Model):
    t = models.DateTimeField("time reserved")
    max_people = models.IntegerField(default = 0) 
    
    def __str__(self):
        return str(self.t)

class Reser(models.Model):
    host_name = models.CharField(max_length = 64)
    host_contact = models.CharField(max_length = 32)
    people = models.IntegerField(default = 1)
    t = models.ForeignKey(TimeSlot, on_delete = models.CASCADE)

    def __str__(self):
        return self.host_name
