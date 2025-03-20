from django.contrib import admin
from django.urls import path
from catalogo.views import *


urlpatterns = [
    path('', index, name= 'index'),
    path('catalogo/',catalogo, name= 'catalogo'),
    path('login/', login, name='login'),
]
