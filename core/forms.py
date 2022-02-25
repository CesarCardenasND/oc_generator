from contextlib import nullcontext
from django.forms import ModelForm, inlineformset_factory
from django.forms.widgets import SelectDateWidget
from .models import User, Concept, PO
from django.forms.models import inlineformset_factory

def user_choices():
    result = []
    for User in User.objects.all():
        result.append((User.id, User.name))
    return result

def concept_choices():
    result = []
    for Concept in Concept.objects.all():
        result.append((Concept.id, Concept.description))
    return result

def concept_choices():
    result = []
    for Concept in Concept.objects.all():
        result.append((Concept.id, Concept.description))
    return result

class regisUser(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'active']

class conceptModelForm(ModelForm):
    class Meta:
        model = Concept
        fields = ["id","Unidad", "Cantidad", "Descripcion", "Precio", "Total", "Notas"]

class poModelForm(ModelForm):
    class Meta:
        model = PO
        fields = ["id","date", "client","project","contact_name","bill_to"]
        fields_classes = {
            'unit': ('Unidad'),
            'quantity': ('Cantidad'),
            'description': ('Descripcion'),
            'unit_price': ('Precio Unitario'),
            'total': ('Total'),
            'notes':('Notas'),
        }
        labels = {
            'date': ('Fecha'),
            'client': ('Cliente'),
            'project': ('Proyecto'),
            'contact_name': ('Contacto'),
            'bill_to': ('Factura'),
        }
