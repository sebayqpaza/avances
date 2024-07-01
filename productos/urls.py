
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_zapatillas, name='lista_zapatillas'),
    path('<int:id>/', views.detalle_zapatilla, name='detalle_zapatilla'),
]
