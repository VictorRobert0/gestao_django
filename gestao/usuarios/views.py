from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256

# Create your views here.



def login(request):
    status = request.GET.get('status')
    return render (request,'login_front/login.html',{'status': status})

    

def cadastro(request):
    status = request.GET.get('status')
    return render (request,'cadastro_front/cadastro.html', {'status': status})


def valida_cadastro(request):
    username = request.POST.get('nome_cad')
    email = request.POST.get('email_cad')
    password = request.POST.get('senha_cad')
    
    usuario = Usuario.objects.filter(email = email)
    
    if len(username.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/usuarios/cadastro/?status=1')
    
    if len(password) < 4:
        return redirect('/usuarios/cadastro/?status=2')
    
    if len(usuario) > 0:
        return redirect('/usuarios/cadastro/?status=3')
    try:
        password = sha256(password.encode()).hexdigest
        usuario = Usuario(username = username, email = email, password = password)
        usuario.save()
        
        return redirect('/usuarios/cadastro/?status=0')
        
    except:
        return redirect('usuarios/cadastro/?status=4')


def valida_login(request):
    email = request.POST.get('email_login')
    password = request.POST.get('senha_login')
    password = sha256(password.encode()).hexdigest()
    

    usuario = Usuario.objects.filter (email= email).filter(password = password)
    
    if len(usuario) == 0:
        return redirect ('/usuarios/login/?status=1')
    elif len(usuario) > 0:
        request.session ['usuario'] = usuario[0].id
        return redirect ('/sistema/home')


def index(request):
    form = Usuario()
    return render (request, 'index.html',{'form': form})
