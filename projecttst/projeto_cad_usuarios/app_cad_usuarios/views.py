# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Usuario # Depois de criar o DB 

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'usuarios/home.html')

def juju(request):
    return render(request,'usuarios/juju.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()
    
    # Codigo para exibir os usuarios ja cadastros abaixo meu bom 
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    
    # Retornar os dados para a pagina de listagem 
    return render(request, 'usuarios/usuarios.html', usuarios)
