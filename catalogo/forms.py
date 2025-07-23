from django import forms
from .models import Libro, Genero, Perfil
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
    nombre_libro = forms.CharField(
        label='Nombre del libro',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'input-control',
            'style': 'width: 40%; background-color: #FFD200; border: 1px solid #ccc; padding: 10px; border-radius: 5px; text-color: white;'
        })
    )
    autor = forms.CharField(
        label='Autor',
        widget=forms.TextInput(attrs={
            'class': 'input-control',
            'style': 'width: 40%; background-color: #FFD200; border: 1px solid #ccc; padding: 10px; border-radius: 5px; text-color: white;'
        })
    )
    edicion = forms.CharField(
        label='Edición',
        widget=forms.TextInput(attrs={
            'class': 'input-control',
            'style': 'width: 40%; background-color: #FFD200; border: 1px solid #ccc; padding: 10px; border-radius: 5px; text-color: white;'
        })
    )
    año = forms.IntegerField(
        label='Año',
        widget=forms.NumberInput(attrs={
            'class': 'input-control',
            'style': 'width: 40%; background-color: #FFD200; border: 1px solid #ccc; padding: 10px; border-radius: 5px; text-color: white;'
        })
    )
    editorial = forms.CharField(
        label='Editorial',
        widget=forms.TextInput(attrs={
            'class': 'input-control',
            'style': 'width: 40%; background-color: #FFD200; border: 1px solid #ccc; padding: 10px; border-radius: 5px; text-color: white;'
        })
    )
    isbn = forms.CharField(
        label='ISBN',
        widget=forms.TextInput(attrs={
            'class': 'input-control',
            'style': 'width: 40%; background-color: #FFD200; border: 1px solid #ccc; padding: 10px; border-radius: 5px; text-color: white;'
        })
    )
    portada = forms.ImageField(
        label='Portada',
        required=False,
        widget=forms.ClearableFileInput(attrs={
            'class': 'input-control',
            'style': 'width: 40%; background-color: #FFD200; border: 1px solid #ccc; padding: 10px; border-radius: 5px; text-color: white;'
        })
    )
    valor_saberes = forms.CharField(
        label='Valor de saberes',
        widget=forms.TextInput(attrs={
            'class': 'input-control',
            'style': 'width: 40%; background-color: #FFD200; border: 1px solid #ccc; padding: 10px; border-radius: 5px; text-color: white;'
        })
    )
    genero = forms.ModelChoiceField(
        queryset=Genero.objects.all(),
        label='Género',
        widget=forms.Select(attrs={
            'class': 'input-control',
            'style': 'width: 40%; background-color: #FFD200; border: 1px solid #ccc; padding: 10px; border-radius: 5px; text-color: white;'
        })
    )

    # estilos de textarea
    resenia = forms.CharField(
        label='Reseña',
        widget=forms.Textarea(attrs={
            'class': 'input-control flex-grow-1',
            'style': 'width: 40%; background-color: #FFD200; border: 1px solid #ccc; border-radius: 5px;',

        })
    )
    
    
    class Meta:
        model = Libro
        fields = '__all__'
        
class PerfilForm(forms.ModelForm):
    nombre = forms.CharField(
        label='Nombre',
        widget=forms.TextInput(attrs={
        'class': 'input-control',
        'style': 'background-color: #D3D3D3; border: 1px solid #ccc; padding: 10px; border-radius: 5px;'
    })
    )
    apellido = forms.CharField(
        label='Apellido',
        widget=forms.TextInput(attrs={
        'class': 'input-control',
        'style': 'background-color: #D3D3D3; border: 1px solid #ccc; padding: 10px; border-radius: 5px;'
    })
    )
    telefono = forms.CharField(
        label='Teléfono',
        widget=forms.TextInput(attrs={
        'class': 'input-control',
        'style': 'background-color: #D3D3D3; border: 1px solid #ccc; padding: 10px; border-radius: 5px;'
    })
    )
    email = forms.EmailField(
    label='Correo electrónico',
    widget=forms.EmailInput(attrs={
        'class': 'input-control',
        'style': 'width: 25%; background-color: #D3D3D3; border: 1px solid #ccc; padding: 10px; border-radius: 5px;'
    })
)
    direccion = forms.CharField(
        label='Dirección',
        widget=forms.TextInput(attrs={
            'class': 'input-control',
            'style': ' background-color: #D3D3D3; border: 1px solid #ccc; padding: 10px; border-radius: 5px;'
        })
    )
    barrio = forms.CharField(
        label='Barrio',
        widget=forms.TextInput(attrs={
            'class': 'input-control',
            'style': 'background-color: #D3D3D3; border: 1px solid #ccc; padding: 10px; border-radius: 5px;'
        })
    )
    edad = forms.IntegerField(
        label='Edad',
        widget=forms.NumberInput(attrs={
            'class': 'input-control',
            'style': 'background-color: #D3D3D3; border: 1px solid #ccc; padding: 10px; border-radius: 5px;'
        })
    )
    class Meta:
        model = Perfil
        fields = ['nombre', 'apellido', 'telefono', 'direccion', 'barrio', 'edad']


