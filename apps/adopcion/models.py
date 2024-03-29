from django.db import models

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad = models.IntegerField()
    telefono = models.CharField(max_length=12)
    email = models.EmailField()
    domilicio = models.TextField()
    
    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos) #Para agregar el nombre de la persona a la caja de seleccion
