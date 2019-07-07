from django.contrib import admin
from .models import Cliente, Cuento, Ventas, Contacto
# Register your models here.
admin.site.register(Cliente)

admin.site.register(Cuento)

admin.site.register(Ventas)

admin.site.register(Contacto)
