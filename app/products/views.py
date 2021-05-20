from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product
from django import forms
from django.contrib import messages
from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse
from datetime import datetime
from django.views.generic import View
# Create your views here.
#proteger de usuarios no autenticados
@login_required(login_url='autenticacion/acceder')
def listado_productos(request):
	products = Product.objects.all()
	# lo manda al template listado.html como products

	return render(request, "products/listado.html", {"products": products})



