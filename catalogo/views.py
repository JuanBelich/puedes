from django.shortcuts import render
from .models import *

# Create your views here.
def catalogo(request):
    libros = Libro.objects.all()
    ctx= {
        "Libros": libros
    }
    return render (request,'catalogo.html',ctx)


def login(request):
    return render(request,'login.html')



def index(request):
    return render(request,'index.html')