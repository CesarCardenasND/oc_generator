from types import TracebackType
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.db.models.fields.files import FileField
from django.db.models.fields.related import ForeignKey
from django.forms import DateField
from datetime import datetime as dttm
from django.utils import timezone

class Concept(models.Model):
    Unidad = models.CharField(max_length=155, null=True, blank=True)
    Cantidad = models.IntegerField(null=True, blank=True)
    Descripcion = models.CharField(max_length=155, null=True, blank=True)
    Precio = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    Total = models.DecimalField(max_digits=12,decimal_places=2, null=True, blank=True) #Unit * Quantity
    Notas = models.CharField(max_length=256, null=True, blank=True)
    PO = models.ForeignKey("PO", on_delete=models.CASCADE, null=True, blank=True)

    def __int__(self):
        return self.id

class User(models.Model):
    name = models.CharField(max_length=155, null=True, blank=True)
    active = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.name

class PO (models.Model):
    client = models.CharField(max_length=155, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    project = models.CharField(max_length=155, null=True, blank=True)
    contact_name = models.CharField(max_length=155, null=True, blank=True)
    bill_to = models.CharField(max_length=155,null=True,blank=True)
    
    def __int__(self):
        return self.id
