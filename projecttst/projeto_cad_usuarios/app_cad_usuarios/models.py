from django.db import models

# Create your models here.
# Essa class me consagrado basicamente vai ser transormada em codigo SQL pelo python
class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255) # Aqui estou definindo a quantidade maxima de caracteres
    idade = models.IntegerField() # Definindo que tem que ser um numero inteiro  
    



# Depois de criar, entre no terminal e de um python3 manage.py makemigrations 
# Depois de criar, de um no terminal novamente python3 manage.py migrate 
    