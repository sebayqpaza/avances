from django.urls import path
from . import views

urlpatterns = [
    path('productos/detalles_zapatilla/<int:zapatilla_id>/', views.detalles_zapatilla, name='detalles_zapatilla'),
    path('', views.lista_zapatillas, name='lista_zapatillas'),
]
