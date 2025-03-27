from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *

# Apartado de Libros

def catalogo(request):
    libros = Libro.objects.all()
    ctx= {
        "Libros": libros
    }
    return render (request,'catalogo.html',ctx)

def agregar_libro(request):
    if request.method == 'POST':
        Libro.objects.create(
            nombre_libro=request.POST.get('nombre_libro'),
            autor=request.POST.get('autor'),
            editorial=request.POST.get('editorial'),
            edicion=request.POST.get('edicion'),
            año=request.POST.get('año'),
            isbn=request.POST.get('isbn'),
            valor_saberes=request.POST.get('valor_saberes')
        )
        return redirect('catalogo')  # Redirige a la vista catalogo
    
    return render(request, 'agregarLibro.html')

def editar_libro(request):
    return render(request, 'agregarLibro.html')

def eliminar_libro(request):
    return render(request, 'agregarLibro.html')




# Apartado de login

def login(request):
    return render(request,'login.html')

def registro(request):
    return render(request,'registro.html')


def index(request):
    return render(request,'index.html')

