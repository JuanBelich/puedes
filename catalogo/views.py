import os
from django.views.decorators.http import require_POST
from django.core.mail import send_mass_mail
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from catalogo.forms import CustomUserCreationForm, CustomAuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, user_passes_test

from catalogo.forms import LibrosForm
from .models import *

# Apartado de Libros

def catalogo(request):
    # Obtiene todos los libros y géneros de la base de datos
    libro = Libro.objects.all()
    generos = Genero.objects.all()
    formulario = LibrosForm()
    ctx= {
        "Libros": libro,
        "Generos": generos,
        'formulario': formulario
    }
    # Renderiza la plantilla 'catalogo.html' con los libros y géneros
    return render (request,'catalogo.html',ctx)

def agregar_libro(request):

    
    formulario= LibrosForm(request.POST, request.FILES) 
    
    if formulario.is_valid():
        # Si el formulario es válido, guarda el libro en la base de datos
        formulario.save()
        # Redirige a la vista del catálogo
        return redirect('catalogo')
    else:
        # Si el formulario no es válido, redirige a la vista del catálogo
        return redirect('catalogo')

def eliminar_libro(request,id):
    libro = Libro.objects.get(id=id)
    if libro.portada:
        imagen_path = os.path.join(settings.MEDIA_ROOT, str(libro.portada))
        if os.path.isfile(imagen_path):
            os.remove(imagen_path)
    libro.delete()
    return redirect('catalogo')



def editar_libro(request,id):
    # Busca el libro por su id
    libros = get_object_or_404(Libro, id=id)
    
    if request.method == 'GET':
        # Si la solicitud es GET, busca el libro por su id
        formulario = LibrosForm(instance=libros)
        # Crea un formulario con los datos del libro    
        contexto= {
            'formulario': formulario,
            "Libros": libros,
            'generos': Genero.objects.all(),
        }
        print(libros.portada.path)
        return render(request, 'editar_libro.html', contexto)
    
    elif request.method == 'POST':
        # Guarda la ruta de la portada anterior antes de actualizar
        portada_anterior = libros.portada.path if libros.portada else None

        # Crea un formulario con los datos enviados
        formulario = LibrosForm(request.POST, request.FILES, instance=libros)
        if formulario.is_valid():
            # Si se subió una nueva portada, elimina la anterior después de guardar
            nueva_portada = 'portada' in request.FILES
            formulario.save()
            if nueva_portada and portada_anterior and os.path.isfile(portada_anterior):
                os.remove(portada_anterior)
            # Redirige al catálogo
            return redirect('catalogo')






# Apartado de login

def singin(request):
    # Verifica si el usuario ya está autenticado
    if request.method == 'GET':
        return render(request, 'singin.html', {
            'form': CustomAuthenticationForm,
        })
    # Si el usuario no está autenticado, intenta autenticarlo
    elif request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            print('usuario no encontrado')
            return render(request, 'singin.html', {
                'form': CustomAuthenticationForm,
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            print('usuario encontrado')
            login(request, user)
            perfil = Perfil.objects.get(user=user)
            print("el grupo de usuario es: ", user.groups.all())
            return render(request, 'profile.html', {
                'user': user,
                'perfil': perfil,
            })

# Apartado de registro
def singup(request):
    if request.method == 'GET':
        print('mostrando formulario')
        return render(request, 'singup.html', {'form':CustomUserCreationForm})

    if request.method == 'POST':
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                user = User.objects.create_user(
                    username=request.POST.get('username'),
                    password=request.POST.get('password1'),
                    email=request.POST.get('email')
                )
                user.save()
                grupo_usuario, creado = Group.objects.get_or_create(name='Usuario')
                user.groups.add(grupo_usuario)
                print("el grupo del usuario es: ", grupo_usuario)
                # Crear el perfil con los datos adicionales
                Perfil.objects.create(
                    user=user,
                    nombre=request.POST.get('nombre'),
                    apellido=request.POST.get('apellido'),
                    telefono=request.POST.get('telefono'),
                    direccion=request.POST.get('direccion'),
                    barrio=request.POST.get('barrio'),
                    edad=request.POST.get('edad'),
                    saber=0  # Valor inicial para saber
                    )
                print(' usuario creado correctamente')
                login(request, user)
                return redirect('singin')

            except IntegrityError:
                print(f'Error al crear el usuario: el usuario ya existe')
                return render(request, 'singup.html', {
                    'form': CustomUserCreationForm,
                    'error': 'El usuario ya existe'
                })

    return render(request, 'singup.html', {
        'form': CustomUserCreationForm,
        'error': 'las contraseñas no coinciden'
    })
    
# Apartado de logout
@login_required
def singout(request):
    logout(request)
    return redirect('index')

# Apartado de perfil
@login_required
def perfil(request):
    if not request.user.is_authenticated:
        return redirect('singin')
    perfil = Perfil.objects.get(user=request.user)
    generos = Genero.objects.all()
    return render(request, 'profile.html', {
        'user': request.user,
        'perfil': perfil,
        "Generos": generos,
    })
    
@login_required
def toggle_favorito(request, libro_id):
    perfil = Perfil.objects.get(user=request.user)
    libro = get_object_or_404(Libro, id=libro_id)
    if libro in perfil.favoritos.all():
        perfil.favoritos.remove(libro)
    else:
        perfil.favoritos.add(libro)
    return redirect('perfil')

def recuperar(request):
    return render(request, 'recuperar.html')

def es_bibliotecario(user):
    return user.groups.filter(name='Bibliotecario').exists()


@user_passes_test(es_bibliotecario)
@require_POST
def agregar_genero(request):
    genero = request.POST.get('genero')
    if genero:
        Genero.objects.create(genero=genero)
    return redirect('perfil')

@user_passes_test(es_bibliotecario)
@require_POST
def editar_genero(request, genero_id):
    genero = get_object_or_404(Genero, id=genero_id)
    nombre = request.POST.get('nombre')
    if nombre:
        genero.nombre = nombre
        genero.save()
    return redirect('perfil')

@user_passes_test(es_bibliotecario)
@require_POST
def eliminar_genero(request, genero_id):
    genero = get_object_or_404(Genero, id=genero_id)
    genero.delete()
    return redirect('perfil')


@user_passes_test(es_bibliotecario)
def buscar_usuario(request):
    usuarios_encontrados = []
    busqueda_realizada = False
    nombre = request.GET.get('nombre', '').strip()
    apellido = request.GET.get('apellido', '').strip()
    if nombre or apellido:
        busqueda_realizada = True
        perfiles = Perfil.objects.all()
        if nombre:
            perfiles = perfiles.filter(nombre__icontains=nombre)
        if apellido:
            perfiles = perfiles.filter(apellido__icontains=apellido)
        usuarios_encontrados = [perfil.user for perfil in perfiles]
    return render(request, 'profile.html', {
        'usuarios_encontrados': usuarios_encontrados,
        'busqueda_realizada': busqueda_realizada,
        'perfil': Perfil.objects.get(user=request.user),
        'user': request.user,
    })

@user_passes_test(es_bibliotecario)
def modificar_saber(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    perfil = Perfil.objects.get(user=usuario)
    if request.method == 'POST':
        nuevo_saber = request.POST.get('nuevo_saber')
        perfil.saber = nuevo_saber
        perfil.save()
    return redirect('buscar_usuario')

@user_passes_test(lambda u: u.groups.filter(name='Bibliotecario').exists())
def enviar_mensaje_todos(request):
    mensaje_enviado = False
    if request.method == 'POST':
        mensaje = request.POST.get('mensaje')
        asunto = "Mensaje de la Biblioteca"
        from_email = 'tucorreo@tudominio.com'  # Cambia esto por tu correo
        usuarios = User.objects.exclude(email='').values_list('email', flat=True)
        mensajes = [(asunto, mensaje, from_email, [email]) for email in usuarios]
        send_mass_mail(mensajes, fail_silently=False)
        mensaje_enviado = True
    # Renderiza el perfil con el mensaje de éxito
    perfil = Perfil.objects.get(user=request.user)
    return render(request, 'profile.html', {
        'perfil': perfil,
        'mensaje_enviado': mensaje_enviado,
        # Agrega aquí otras variables de contexto que uses en tu perfil
    })
    
# ===========================
# MUY IMPOTANTE:
# CONFIGURAR DATOS DE MAILS PARA ENVIO DE NOTIFICACIONES
# Asegúrate de configurar los datos de tu correo en settings.py
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'tucorreo@gmail.com'         # Tu correo
# EMAIL_HOST_PASSWORD = 'tu_contraseña_de_app'   # Contraseña de aplicación (no la de tu cuenta)
# DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
# ===========================




#Apartado general

def index(request):
    libros = Libro.objects.all()
    ctx= {
        "Libros": libros
    }
    return render (request,'index.html',ctx)

def about(request):
    return render (request, "about.html")

def resenia(request, id):
    libro = get_object_or_404(Libro, id=id)
    ctx = {
        'Libro': libro
    }
    return render(request, 'resenia.html', ctx)