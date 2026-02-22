# models.py

from django.db import models

class Bus(models.Model):
    bus_no=models.CharField(max_length=100)
    bus_name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.bus_name