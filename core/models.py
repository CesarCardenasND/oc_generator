from types import TracebackType
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.enums import Choices
from django.db.models.fields.files import FileField
from django.db.models.fields.related import ForeignKey
from django.forms import DateField
from paranoid_model.models import Paranoid
from paranoid_model.manager import ParanoidManager
from paranoid_model.queryset import ParanoidQuerySet
from datetime import datetime as dttm

class Concept(Paranoid):
    unit = models.CharField(max_length=155, null=True, blank=True)
    quantity = models.IntegerField(max_length=155, null=True, blank=True)
    description = models.CharField(max_length=155, null=True, blank=True)
    unit_price = models.DecimalField(decimal_places=2)
    total = models.DecimalField(decimal_places=2) #Unit * Quantity

    def __str__(self):
        return self.name

class User(Paranoid):
    name = models.CharField(max_length=155, null=True, blank=True)
    active = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.name

class PO (Paranoid):
    date = models.DateField(auto_now_add=True)
    client = models.ForeignKey("User", on_delete=models.CASCADE, null=True, blank=True)
    project = models.CharField(max_length=155, null=True, blank=True)
    contact_name = models.CharField(max_length=155, null=True, blank=True)
    invoice_name = models.CharField(max_length=155, null=True, blank=True)
    bill_to = models.CharField(max_length=155,null=True,blank=True)
    concept = models.ForeignKey(Concept, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
