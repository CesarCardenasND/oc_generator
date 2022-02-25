from unicodedata import name
from django.forms.forms import Form
from django.urls import path
from .views import index, register_oc, register_concept
from django.forms import forms
from core import views

urlpatterns = [
    path('', index, name='index'),
    path('register_oc/', register_oc, name='register_oc'),
    path('register_concept/', register_concept, name='register_concept'),
    path('po_pdf', views.po_pdf, name='po_pdf')
]