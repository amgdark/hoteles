from django.db import models

class Ciudad(models.Model):
    nombre = models.CharField(max_length=120)
    
    def __str__(self):
        return self.nombre

class DatosHotel(models.Model):
	nombre = models.CharField('Nombre',max_length=200)
	telefono = models.CharField('Teléfono',max_length=13)
	direccion = models.CharField('Dirección',max_length=100)
	colonia = models.CharField(max_length=50)
	ciudad = models.ForeignKey(Ciudad)
	
	def __str__(self):
		return self.nombre