from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # Rota para a página inicial
    path('', views.home, name='home'),

    # Rota para a página "maconha"
    path('juju/', views.juju, name='juju'), 
    # http://127.0.0.1:8000/juju/
    
    #R Rota of users
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    
]
