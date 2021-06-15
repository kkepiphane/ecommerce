from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Utilisateur)
admin.site.register(Produit)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Element)
admin.site.register(AdresseCourse)