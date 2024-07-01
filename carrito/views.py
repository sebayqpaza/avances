from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from productos.models import Zapatilla

@login_required
def agregar_al_carrito(request, zapatilla_id):
    zapatilla = get_object_or_404(Zapatilla, id=zapatilla_id)
    carrito = request.session.get('carrito', [])
    carrito.append(zapatilla.id)
    request.session['carrito'] = carrito
    return redirect('detalle_zapatilla', zapatilla_id=zapatilla.id)

@login_required
def ver_carrito(request):
    carrito = request.session.get('carrito', [])
    zapatillas = Zapatilla.objects.filter(id__in=carrito)
    return render(request, 'carrito/ver_carrito.html', {'zapatillas': zapatillas})
