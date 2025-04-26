import os
from django.conf import settings
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
            valor_saberes=request.POST.get('valor_saberes'),
            portada = request.FILES.get('portada')

        )
        return redirect('catalogo')  # Redirige a la vista catalogo
    
    return render(request, 'agregarLibro.html')

def eliminar_libro(request,id):
    libro = Libro.objects.get(id=id)
    if libro.portada:
        imagen_path = os.path.join(settings.MEDIA_ROOT, str(libro.portada))
        if os.path.isfile(imagen_path):
            os.remove(imagen_path)
    libro.delete()
    return redirect('catalogo')



def editar_libro(request,id):
    return HttpResponse(f"editar el id: {id}")






# Apartado de login

def login(request):
    return render(request,"login.html")

def singup(request):
    return render(request, 'singup.html')

def recuperar(request):
    return render(request, 'recuperar.html')


#Apartado general

def index(request):
    libros = Libro.objects.all()
    ctx= {
        "Libros": libros
    }
    return render (request,'index.html',ctx)

def about(request):
    return render (request, "about.html")