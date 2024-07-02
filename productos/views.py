
from django.shortcuts import render, get_object_or_404 ,redirect
from .models import Zapatilla
from carrito.carrito import Carrito

def detalle_zapatilla(request, id):
    zapatilla = get_object_or_404(Zapatilla, id=id)
    return render(request, 'productos/detalle_zapatilla.html', {'zapatilla': zapatilla})

def lista_zapatillas(request):
    zapatillas = Zapatilla.objects.all()
    return render(request, 'productos/lista_zapatillas.html', {'zapatillas': zapatillas})

def agregar_al_carrito(request, zapatilla_id):
    carrito = Carrito(request)
    zapatilla = get_object_or_404(Zapatilla, id=zapatilla_id)
    carrito.add(zapatilla=zapatilla)
    return redirect('detalle_zapatilla', id=zapatilla.id)