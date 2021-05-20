from django.urls import path
from .views import *

urlpatterns = [
	#url creada para apuntar desde cualquier template { url listado productos }
	path('', listado_productos, name='listado_productos'),
	
	]