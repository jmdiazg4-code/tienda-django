from django.urls import path
from .views import *

urlpatterns = [
	
	path('<producto>', carrito, name='carrito'),
	path('<int:id>', comprarArticulo, name='comprarArticulo'),

]