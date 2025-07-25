from django.contrib import admin
from django.urls import path
from catalogo.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name= 'index'),
    path('singin', singin, name='singin'),
    path('singup/', singup, name='singup'),
    path('perfil/', perfil, name='perfil'),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('logout/', singout, name='singout'),
    path('catalogo/',catalogo, name= 'catalogo'),
    path('recuperar/', recuperar, name='recuperar'),
    path('agregar_libro/', agregar_libro, name='agregar_libro'),
    path('eliminar_libro/<id>', eliminar_libro, name='eliminar_libro'),
    path('editar_libro/<id>', editar_libro, name='editar_libro'),
    path('about/', about, name='about'),
    path('resenia/<id>', resenia, name='resenia'),
    path('favorito/<int:libro_id>/', toggle_favorito, name='toggle_favorito'),
    path('buscar_usuario/', buscar_usuario, name='buscar_usuario'),
    path('modificar_saber/<int:user_id>/', modificar_saber, name='modificar_saber'),
    path('enviar_mensaje_todos/', enviar_mensaje_todos, name='enviar_mensaje_todos'),
    path('agregar_genero/', agregar_genero, name='agregar_genero'),
    path('editar_genero/<int:genero_id>/', editar_genero, name='editar_genero'),
    path('eliminar_genero/<int:genero_id>/', eliminar_genero, name='eliminar_genero'),
    path('enviar_mensaje_personalizado/', enviar_mensaje_personalizado, name='enviar_mensaje_personalizado'),]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)