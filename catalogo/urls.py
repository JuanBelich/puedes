from django.contrib import admin
from django.urls import path
from catalogo.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name= 'index'),
    path('catalogo/',catalogo, name= 'catalogo'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
    path('agregar_libro/', agregar_libro, name='agregar_libro'),
    path('eliminar_libro/<id>', eliminar_libro, name='eliminar_libro'),
    path('editar_libro/<id>', editar_libro, name='editar_libro'),
    
    
] # + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)