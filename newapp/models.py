# models.py

from django.db import models

class Bus(models.Model):
    BUS_TYPE = [
         ('', 'Select Bus Type'),
        ('AC', 'AC'),
        ('NON-AC', 'NON-AC'),
        ('SLEEPER', 'Sleeper'),
    ]
    bus_no=models.CharField(max_length=100)
    bus_name = models.CharField(max_length=100)
    bus_type= models.CharField(max_length=100,choices=BUS_TYPE)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    arrival_time=models.TimeField()
    departure_time=models.TimeField()
    price = models.IntegerField()

    def __str__(self):
        return self.bus_name