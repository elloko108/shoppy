from django.contrib import admin
from .models import Client


@admin.register(Client)
class AdminClient(admin.ModelAdmin):
	list_display = ('nombre', 'telefono', 'email',)
	list_filter = ('nombre',)
