from django.urls import path
from app_cad_usuarios import views # Estou importando o lindo arquivo views que esta na pasta app_cad_usuarios
urlpatterns = [
    # rota, view responsavel, nome de referencia 
    path('',views.home,name='home'),
]
