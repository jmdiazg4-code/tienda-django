from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from products.models import Product
from django.contrib import messages
from .models import orden
from django import forms
from datetime import datetime
from django.views.generic import View
from django.template import engines
import json


# Create your views here.


class hacerCompra(forms.Form):
	nombre = forms.CharField(label='Nombre Completo')
	email = forms.EmailField(label='E-mail')
	telefono = forms.CharField(label='Teléfono o Celular')
	#status = forms.CharField(
    #    widget=forms.TextInput(attrs={'readonly':'readonly'})
    #)


class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields= '__all__'


def carrito(request, producto):
	print(producto)
	objeto= Product.objects.get(id=producto)
	print(objeto.price)
	if request.method == 'POST':
		form = hacerCompra(request.POST)
		if form.is_valid():
			name = form.cleaned_data['nombre']
			email = form.cleaned_data['email']
			mobile = form.cleaned_data['telefono']
			print('entro a carrito')
			print(name)
			print(email)
			print(mobile)
			

			usuario = orden(customer_name=name, customer_email=email,
						customer_mobile=mobile, status='CREATED',
						created_at='',update_at='', url_payment='', 
						product=objeto.name, total=objeto.price)
			
			
			print(usuario.customer_name)
			print(usuario.customer_email)
			print(usuario.customer_mobile)
			print(usuario.status)
			print(usuario.created_at)
			print(usuario.update_at)
			print(usuario.url_payment)
			print(usuario.product)
			print(usuario.total)

			if usuario is not None:
				messages.success(request, F"Guardado {name}")
				#el formulario se pinta el html pedido de la CARPETA CART
				return render(request, "cart/pedido.html", {"form77":form ,"usuario": usuario, "objeto":objeto })
			else:
				messages.error(request, F"Los datos son incorrectos is none {name}")
		else:
			messages.error(request, "Los datos son incorrectos no valido")
	
	form = hacerCompra()
	return render(request, "cart/pedido.html", {"form77": form })


def comprarArticulo(request, id):
	producto = Product.objects.get(id =  id)
	if request.method == 'GET':
		form = ProductForm(instance=producto)
		contexto={
			'seleccionado': form
		}
	return redirect('carrito', producto)


