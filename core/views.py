from email import utils
from msilib.schema import ListView
from re import T
from venv import create
from django import forms
from django.shortcuts import render, redirect
from reportlab.lib import utils
from django.http import FileResponse, HttpResponse

import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from .models import PO, Concept, User
from .forms import conceptModelForm, poModelForm
from django.forms import inlineformset_factory

# Create your views here.

def index(request):
    #Function Code
    POS = PO.objects.all()
    print(POS)
    return render(request, 'home.html', {'PO':POS})

def register_oc(request):
    #Function Code
    po = PO()
    form = poModelForm(instance=po)
    conceptFormSet = inlineformset_factory(PO, Concept, fields='__all__', extra=1, can_delete=False)

    if request.method == "POST":
        form = poModelForm(request.POST)
        formset = conceptFormSet(request.POST, request.FILES)

        if form.is_valid():
            created_po = form.save(commit=False)
            formset = conceptFormSet(request.POST, request.FILES, instance = created_po)
            
            if formset.is_valid():
                created_po.save()
                formset.save()
                return redirect('index')
    else:
        form = poModelForm(instance=po)
        formset = conceptFormSet()

    return render(request, 'register_oc.html', {'form':form,'formset':formset})
            


def register_concept(request, id):
    #Function Code
    concepts = Concept.objects.all()
    if request.method == 'POST':
        form = conceptModelForm(request.POST)
        if form.is_valid():
            return redirect('index')
    else:
        form = conceptModelForm()
    return render(request, 'register_concept.html', {'form':form})

def po_pdf(request):
    #create bytestream buffer
    pos = PO.objects.all()
    buf = io.BytesIO()
    #create canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    #create text object
    textob = c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica", 14)
    #add text
    lines = []
    
    for item in pos:
        lines.append(item.client)
        date_str = str(item.date)
        lines.append(date_str)
        lines.append(item.project)
        lines.append(item.contact_name)
        lines.append(item.bill_to)
        #lines.append(item.Concept.unit)
        lines.append(" ")

    #line loop
    for line in lines:
        textob.textLine(line)
    #END
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=False, filename='po_pdf.pdf')