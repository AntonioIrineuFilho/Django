from django.shortcuts import render
from django.http import HttpResponse
from . import services

def index(request):
    # services.cadastrar_usuario('antzin', 'antonio@gmail.com', 'antzin123')
    # services.atualizar_usuario('antzin', username_novo='antzin_atualizado')
    services.criar
    return HttpResponse('<h1>Caronas</h1>')
