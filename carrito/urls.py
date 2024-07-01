from django.urls import path
from . import views

urlpatterns = [
    path('agregar/<int:zapatilla_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('', views.ver_carrito, name='ver_carrito'),
]
