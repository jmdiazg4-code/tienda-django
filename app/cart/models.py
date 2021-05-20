from django.db import models
from django import forms
import os


# Create your models here.
class orden(models.Model):
	customer_name = models.CharField(max_length=80, null=False ,verbose_name='Nombre Completo')
	customer_email = models.EmailField(max_length=120, null=False, verbose_name='E-mail')
	customer_mobile = models.CharField(max_length=40, null=False, verbose_name='Celular')
	status = models.CharField(max_length=20, null=False, verbose_name='Estado del Pedido')
	created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
	update_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de actualizacion')
	url_payment = models.URLField(max_length=500)
	product = models.CharField(max_length=100, null=False, verbose_name='Producto de la compra')
	imagen=models.ImageField(default=False)
	total = models.FloatField(default=True)
	


	def __str__(self):
		return self.customer_name


	class Meta:
		db_table= 'orders'
		verbose_name ='Orden'
		verbose_name_plural = 'Ordenes'
		ordering =['id']
