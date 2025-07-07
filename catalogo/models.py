from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Genero(models.Model):
    genero = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.genero
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'

class Libro(models.Model):
    nombre_libro=models.CharField(max_length=50,null=False)
    autor=models.CharField(max_length= 50,null=False)
    editorial=models.CharField(max_length=50)
    edicion=models.CharField(max_length=50)
    año=models.CharField(max_length=7)
    isbn=models.CharField(max_length=50)
    portada = models.ImageField(upload_to='portada/', blank=True, null=True)
    valor_saberes=models.BigIntegerField(null=False)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, default=0)
    resenia = models.TextField(null=True, blank=True)

    

    def __str__(self):
        return self.nombre_libro
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
    
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    direccion = models.CharField(max_length=255)
    barrio = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    saber= models.IntegerField(default=0)
    favoritos = models.ManyToManyField('Libro', blank=True, related_name='usuarios_favoritos')
    
    def __str__(self):
        return self.user.username
    