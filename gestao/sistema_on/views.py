from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.
def home (request):
    return render(request,'principal_front/home.html' )


def cadastrar_servico(request):
    return render (request, 'principal_front/sistema_servico.html')