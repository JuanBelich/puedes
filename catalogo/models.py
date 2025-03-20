from django.db import models

# Create your models here.
class Libro(models.Model):
    nombre_libro=models.CharField(max_length=50,null=False)
    autor=models.CharField(max_length= 50,null=False)
    editorial=models.CharField(max_length=50)
    edicion=models.CharField(max_length=50)
    año=models.CharField(max_length=7)
    isbn=models.CharField(max_length=50)
    valor_saberes=models.BigIntegerField(null=False)
    # preguntar a los bibliotecarios o administradores que datos sobre libros mostrar en las tablas

    def __str__(self):
        return self.nombre_libro
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        