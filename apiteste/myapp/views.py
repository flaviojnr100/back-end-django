from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes

from .models import Usuario

from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import redirect
# Create your views here.




@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def inicio(request):
    usuarios = Usuario.objects.all()

    return render(request,'inicio.html',{'usuarios':usuarios})

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def ver(request,id):
    usuario = Usuario.objects.filter(id=id).get()
    return render(request,'ver.html',{'usuario':usuario})

def cadastro(request):
    return render(request,'cadastro.html')


def editar(request,id):
    usuario = Usuario.objects.filter(id=id).get()
    return render(request,'editar.html',{'usuario':usuario})


def inicio(request):
    usuarios = Usuario.objects.all()
    return render(request,'inicio.html',{'usuarios':usuarios})

@api_view(["POST"])
@csrf_exempt
def salvar(request):
    nome = request.POST['nome']
    sobrenome = request.POST['sobrenome']
    email = request.POST['email']

    usuario = Usuario(nome=nome,sobrenome=sobrenome,email=email)
    usuario.save()
    return redirect('/')


@csrf_exempt
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def deletar(request,id):
    if request.method == "POST" and request.POST['_method'] == "DELETE":

        usuario = Usuario.objects.filter(id=id)
        usuario.delete()
        return redirect('/')
