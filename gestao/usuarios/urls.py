from django.urls import path, include
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadusuario'),
    path('login/', views.login, name='arealogin'),
    path('validar_cadastro/', views.valida_cadastro, name = 'valida_cadastro'),
    path('validar_login/', views.valida_login, name = 'valida_login'),
    path('', views.index),
]
