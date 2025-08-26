from django.shortcuts import render
from . import services

# Create your views here.

def index(request):
    return render(request, 'index.html') # renderizar a requisição com a página HTML

def calcular_imc(request):
    altura = float(request.POST.get('altura')) # pega a altura pela requisição do formulário(action) pelo nome atribuido no template
    peso = float(request.POST.get('peso')) # pega a altura pela requisição do formulário(action) pelo nome atribuido no template
    contexto = services.calcular_imc(altura, peso)
    return render(request, 'imc.html', contexto) # os nomes dos valores do dict serão utilizados no tmeplate imc.html
