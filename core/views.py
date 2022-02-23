from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from core.models import User

# Create your views here.
def index(request):
    #Function Code
    Users=User.objects.all()
    print(Users)
    return render(request, 'home.html', {'Users':Users})

def register(request):
    #Function Code
    if request.method == 'POST':
        form = regisUser(request.POST)
        if form.is_valid():
            return redirect('index')
    else:
        form = regisUser()
    return render(request, 'registro.html', {'form':form})

def register_po(request):
    #Function Code
    if request.method == 'POST':
        form = regisPO(request.POST)
        if form.is_valid():
            return redirect('index')
    else:
        form = regisPO()
    return render(request, 'registro_po.html', {'form':form})

def register_concept(request):
    #Function Code
    if request.method == 'POST':
        form = regisConcept(request.POST)
        if form.is_valid():
            return redirect('index')
    else:
        form = regisConcept()
    return render(request, 'registro_concept.html', {'form':form})