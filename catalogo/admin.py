from django.contrib import admin
from catalogo.models import Libro,Genero

# Register your models here.
admin.site.register(Libro)
admin.site.register(Genero)