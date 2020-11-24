"""apiteste URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import cadastro, salvar, inicio, editar, atualizar, deletar, ver

urlpatterns = [
    path('admin/', admin.site.urls),

    path('cadastro',cadastro,name='cadastro'),
    path('salvar/', salvar,name='salvar'),
    path('', inicio,name='inicio'),
    path('editar/<int:id>', editar,name='editar'),
    path('atualizar/<int:id>', atualizar,name='atualizar'),
    path('deletar/<int:id>', deletar,name='deletar'),
    path('ver/<int:id>', ver,name='ver'),

]


