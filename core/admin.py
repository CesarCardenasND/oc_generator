from django.contrib import admin
from .models import User, Concept, PO
# Register your models here.

admin.site.register(User)
admin.site.register(Concept)
admin.site.register(PO)
