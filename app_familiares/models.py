from django.db import models

# Create your models here.
class Yo(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField()

class Familiar(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField()
    parentesco = models.CharField(max_length=64, null=True, blank=True)
    yo = models.ForeignKey(Yo, on_delete=models.CASCADE)