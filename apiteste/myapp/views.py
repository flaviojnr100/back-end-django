from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.contrib.auth import authenticate,login as lg,logout

from .models import Usuario

from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import redirect
# Create your views here.



def do_login(request):
    usuario = authenticate(username=request.POST['nome'],password=request.POST['senha'])
    if usuario is not None:
        lg(request,usuario)
        return redirect('/')

def do_logout(request):
    logout(request)
    return redirect('/login')

def cadastro_login(request):
    return render(request,'cadastroLogin.html')

def salvar_login(request):
    usuario = User.objects.create_user(request.POST['nome'],request.POST['email'],request.POST['senha'])
    return redirect('/login')

@login_required
def inicio(request):
    usuarios = Usuario.objects.all()

    return render(request,'inicio.html',{'usuarios':usuarios})


@login_required
def ver(request,id):
    usuario = Usuario.objects.filter(id=id).get()
    return render(request,'ver.html',{'usuario':usuario})


@login_required
def cadastro(request):
    return render(request,'cadastro.html')

@login_required
def editar(request,id):
    usuario = Usuario.objects.filter(id=id).get()
    return render(request,'editar.html',{'usuario':usuario})

@login_required
def inicio(request):
    usuarios = Usuario.objects.all()
    return render(request,'inicio.html',{'usuarios':usuarios})


@csrf_exempt
def salvar(request):
    nome = request.POST['nome']
    sobrenome = request.POST['sobrenome']
    email = request.POST['email']

    usuario = Usuario(nome=nome,sobrenome=sobrenome,email=email)
    usuario.save()
    return redirect('/')


@csrf_exempt

def atualizar(request,id):

    if request.method == 'POST' and request.POST['_method'] == "PUT":
        nome = request.POST['nome']
        sobrenome = request.POST['sobrenome']
        email = request.POST['email']

        usuario = Usuario.objects.filter(id=id).get()
        usuario.nome = nome
        usuario.sobrenome = sobrenome
        usuario.email = email
        usuario.save()
        return redirect('/')




@csrf_exempt

def deletar(request,id):
    if request.method == "POST" and request.POST['_method'] == "DELETE":

        usuario = Usuario.objects.filter(id=id)
        usuario.delete()
        return redirect('/')

def login(request):
    return render(request,'login.html')