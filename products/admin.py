from django.contrib import admin
from .models import Product, Favorito
# Register your models here.

#admin.site.register(Product)
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
	list_display = ('id','producto', 'categoria','precio',)
	list_filter = ('producto', 'categoria',)

@admin.register(Favorito)
class AdminFavorito(admin.ModelAdmin):
	list_display = ('user', 'product',)
	list_filter = ('user', 'product',)
	