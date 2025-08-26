from django.shortcuts import render
from . import services

# Create your views here.

def index(request):
    return render(request, 'enquetes/index.html')

def resultado(request):
    resultado = int(request.POST.get("radio")) # o atributo name do HTML é o que é recebido no request.GET.get
    services.votar(resultado)
    contexto = services.resultado()
    return render(request, 'enquetes/resultado.html', contexto)