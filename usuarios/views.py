
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_zapatillas')  # Redirige a la vista principal después de registrarse
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})
