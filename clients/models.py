from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Client(models.Model):
	nombre = models.CharField(max_length=100)
	telefono = models.IntegerField(unique=True)
	email = models.EmailField(max_length=255)
	domicilio = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

	class Meta:
		ordering=('nombre',)