from django.shortcuts import render
from . import services

def index(request):
    return render(request, 'biblioteca/index.html')

def cadastrar_leitor(request):
    nome = request.GET.get("nome")
    email = request.GET.get("email")
    if (nome and email):
        services.cadastrar_leitor(nome, email)
        return render(request, "biblioteca/home.html")