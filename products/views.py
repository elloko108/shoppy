from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import (
	render, 
	get_object_or_404,
	redirect
)

from django.shortcuts import loader

from django.views.generic import ListView
from django.views.generic.detail import DetailView
#para el logueo y deslogueo del sistema
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
#para el formulario de alta y los modelos de tabla
from .models import Product
from .forms import Productoform
#para la vista de table2
from .tables import ProductsTable
from django_tables2 import RequestConfig






# Create your views here.

# def hola_mundo(request):
# 	product = Product.objects.order_by('producto')
# 	template = loader.get_template('index.html')
# 	context = {
# 		'productos':product
# 	}	
# 	return HttpResponse(template.render(context, request))
# 	#return render(request, 'index.html')



# def productodetalle(request, pk):
# 	producto = get_object_or_404(Product, pk=pk)
# 	template = loader.get_template('productodetail.html')
# 	context = {
# 		'product': producto
# 	}
# 	return HttpResponse(template.render(context, request))


class Productolista(ListView):
	model = Product


class Detallesproductos(DetailView):
	model = Product
		

def producto_nuevo(request):
	formulario = Productoform(request.POST, request.FILES)
	if request.method == "POST":
		if formulario.is_valid():
			product = formulario.save(commit=False)
			product.save()
			return HttpResponseRedirect('/')
	else:
		form = Productoform()

	template = loader.get_template('new_product.html')
	context = {
		'form' : formulario
		}
	return HttpResponse(template.render(context, request))


def auth_login(request):
	if request.method == "POST":
		action = request.POST.get('action', None)
		username = request.POST.get('username', None)
		password = request.POST.get('password', None)


		if action == 'signup':
			user = User.objects.create_user(username=username,
										password=password)
			user.save()

		if action == 'login':
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('/')
	
	context={}
	return render(request, 'login/login.html', context)


def productstables(request):
	productos = Product.objects.all()
	tabla = ProductsTable(productos)
	RequestConfig(request).configure(tabla)

	return render(request, 'products_tables.html', 
		{'productstables': tabla})



