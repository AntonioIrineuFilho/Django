from . import views
from django.urls import path

app_name = 'caronas'

urlpatterns = [
    path('', views.index, name='index'),
]