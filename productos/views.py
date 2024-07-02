from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Zapatilla

def lista_zapatillas(request):
    zapatillas = Zapatilla.objects.all()
    return render(request, 'productos/lista_zapatillas.html', {'zapatillas': zapatillas})

def detalles_zapatilla(request, zapatilla_id):
    zapatilla = get_object_or_404(Zapatilla, id=zapatilla_id)
    return render(request, 'productos/detalles_zapatilla.html', {'zapatilla': zapatilla})
