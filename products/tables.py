from django.shortcuts import render

import django_tables2 as tables #usa alias para django_tables2 con tables
from .models import Product


class ProductsTable(tables.Table):
	

	class Meta:
		model = Product #modelo de donde hereda la clase
		exclude = ('imagen', )
		attrs = {'class': 'table'} #configurar el tipo de tabla CSS