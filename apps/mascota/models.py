from django.db import models

from apps.adopcion.models import Persona

class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return '{}'.format(self.nombre)
        
class Mascota (models.Model):
    folio = models.CharField(max_length=10, primary_key=True,default="", editable=True)
    nombre = models.CharField(max_length=50) #Recibe una cadena de maximo 50 digitos. Tipo de dato
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField() #Tipo de dato entero
    fecha_rescate = models.DateField() #Otro tipo de dato
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE) #Relacion uno a muchos
    vacuna = models.ManyToManyField(Vacuna)