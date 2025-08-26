from . import views
from django.urls import path

app_name = "biblioteca"

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.cadastrar_leitor, name='cadastrar_leitor')
]