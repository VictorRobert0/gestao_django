from django.urls import path, include
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('home/',views.home , name='home'),
    path('cadastrar_servico/', views.cadastrar_servico, name='cadastrar_servico')
]
