from __future__ import unicode_literals

from django.db import models
from clients.models import Client

# Create your models here.


class Product(models.Model):
	
	producto = models.CharField(max_length=255)
	descripcion = models.CharField(max_length=255)
	categoria = models.CharField(max_length=255)
	precio = models.DecimalField(max_digits=15, decimal_places=2)
	imagen = models.ImageField(blank=True)

	def __str__(self):
		return self.producto


	class Meta: 
		ordering=('id',)


class Favorito(models.Model):
	user = models.ForeignKey(Client)
	product = models.ForeignKey(Product)

	class Meta:
		verbose_name = 'Favoritos'
		verbose_name_plural = 'Favoritos'

	def __str__(self):
		return '%s %s' % (self.user.nombre, self.product.descripcion)



