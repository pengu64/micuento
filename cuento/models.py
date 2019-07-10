from django.db import models
from decimal import *
# Create your models here.
class Cliente(models.Model):
	Nombre = models.CharField(max_length=40)
	Apellido_p = models.CharField(max_length=40)
	Apellido_m = models.CharField(max_length=40)
	email = models.EmailField(max_length=50)
	password = models.CharField(max_length=256)
	Ciudad = models.CharField(max_length=50)
	Alcaldia = models.CharField(max_length=50)
	Direccion = models.CharField(max_length=120)
	CPostal = models.IntegerField(max_length=7)
	Genero = models.CharField(max_length=1)
	Fecha_subscripcion = models.DateField(auto_now_add=True)
	Telefono = models.CharField(max_length=14)
	Nombre_p = models.CharField(null=True, max_length=20)
	Genero_p = models.CharField(null=True, max_length=4)
	Ciudad_p = models.CharField(null=True, max_length=20)
	Pais_p = models.CharField(null=True, max_length=15)
	Ojos_p = models.CharField(null=True, max_length=10)
	Color_pelo_p = models.CharField(null=True, max_length=10)
	Tipo_pelo_p =models.CharField(null=True, max_length=10)
	Piel_p = models.CharField(null=True, max_length=10)
	Gafas_p = models.BooleanField(null=True)
	
	#def __str__():
	#	return "{} {}".format(self.Nombre, self.Apellido_p)

	
class Cuento(models.Model):
	Titulo = models.CharField(max_length=200)
	Contenido = models.TextField(max_length=200000)
	Precio = models.DecimalField(max_digits=10, decimal_places=2)
	#ventas = models.ManyToManyField(Ventas)
	#def __str__(self):
	#	return self.Titulo
	
class Ventas(models.Model):
	Fecha_compra = models.DateField(null=True, blank=True)
	Num_cuentos = models.IntegerField(max_length=6)
	Venta_total = models.DecimalField(max_digits=10, decimal_places=2)
	Id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	IP = models.BooleanField(null=True)
	cuento = models.ManyToManyField(Cuento)
	
	#def __str__(self):
	#	return str(self.id)
	
# class Acceso_cuenta(models.Model):
#	Fecha_acceso = models.DateField(null=True, blank=True)
#	Fecha_desconexion = models.DateField(null=True, blank=True)
#	Id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	
class Contacto(models.Model):
	Nombre = models.CharField(max_length=40)
	Apellido_p = models.CharField(max_length=40)
	Apellido_m = models.CharField(max_length=40)
	email = models.EmailField(max_length=50)
	telefono = models.BigIntegerField(max_length=14)
	mensaje = models.TextField(max_length=2000)
	fecha = models.DateField(auto_now_add=True)
