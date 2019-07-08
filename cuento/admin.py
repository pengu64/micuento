from django.contrib import admin
from .models import Cliente, Cuento, Ventas, Contacto
# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
	list_display = ("Nombre","Apellido_p","Apellido_m","email","password","Ciudad","Alcaldia","Direccion","CPostal","Genero","Fecha_subscripcion","Telefono","Nombre_p","Genero_p","Ciudad_p","Pais_p","Ojos_p","Color_pelo_p","Tipo_pelo_p","Piel_p","Gafas_p")
admin.site.register(Cliente, ClienteAdmin)

class CuentoAdmin(admin.ModelAdmin):
	list_display = ("Titulo","Contenido","Precio")
admin.site.register(Cuento, CuentoAdmin)

class VentasAdmin(admin.ModelAdmin):
	list_display = ("id","Fecha_compra","Num_cuentos","Venta_total","Id_cliente","IP")
admin.site.register(Ventas, VentasAdmin)

class ContactoAdmin(admin.ModelAdmin):
	list_display = ("Nombre","Apellido_p","Apellido_m","email","telefono","mensaje","fecha")
admin.site.register(Contacto, ContactoAdmin)
