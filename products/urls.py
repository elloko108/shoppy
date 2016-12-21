from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns =  [
	#url(r'^$', views.hola_mundo, name='hola'),
	url(r'^login/$', views.auth_login, name='Logueo'),
	url(r'^logout$', auth_views.logout, {'next_page': '/'} , name='logout'),
	url(r'^$', views.Productolista.as_view(), name='hola'),
	url(r'^productos/(?P<pk>[0-9]+)/$', views.Detallesproductos.as_view(), name='detalle'),
	url(r'^productos/nuevo/', views.producto_nuevo, name='nuevo'),
	url(r'^productos/tabla/', views.productstables, name='tabla'),
]