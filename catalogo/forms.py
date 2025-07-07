from django import forms
from .models import Libro
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={
            'class': 'input-control'
        })
    )
    
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'input-control'
        })
    )
    
class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Nombre de usuario',
        widget=forms.TextInput(attrs={
            'class': 'input-control'
        })
    )
    
    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={
            'class': 'input-control'
        })
    )
    
    apellido = forms.CharField(
        label='Apellido',
        widget=forms.TextInput(attrs={
            'class': 'input-control'
        })
    )
    
    telefono = forms.CharField(
        label='Teléfono',
        widget=forms.TextInput(attrs={
            'class': 'input-control',
            'type': 'tel'
        })
    )
    
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={
            'class': 'input-control'
        })
    )
    direccion = forms.CharField(
        label='Dirección',
        widget=forms.TextInput(attrs={
            'class': 'input-control'
        })
    )
    
    barrio = forms.CharField(
        label='Barrio',
        widget=forms.TextInput(attrs={
            'class': 'input-control'
        })
    )
    
    edad = forms.IntegerField(
        label='Edad',
        widget=forms.NumberInput(attrs={
            'class': 'input-control'
        })
    )
    
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'input-control'
        })
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={
            'class': 'input-control'
        })
    )
    
    
    
    
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields

class LibrosForm(forms.ModelForm):
    
    class Meta:
        model = Libro
        fields = ['nombre_libro', 'autor', 'edicion', 'año', 'editorial' ,'isbn','portada', 'valor_saberes','genero','resenia']


