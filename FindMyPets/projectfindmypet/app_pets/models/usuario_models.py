from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    telefone = models.CharField(max_length=20, null=True)
    data_nascimento = models.DateField(null=True)
    endereco_logradouro = models.CharField(max_length=100, null=True)
    endereco_bairro = models.CharField(max_length=100, null=True)
    endereco_municipio = models.CharField(max_length=100, null=True)
    endereco_estado = models.CharField(max_length=100, null=True)
    endereco_cep = models.CharField(max_length=100, null=True)
    endereco_numero = models.CharField(max_length=100, null=True)
    endereco_complemento = models.CharField(max_length=100, null=True)
    forcar_alterar_senha = models.BooleanField(default=False)
    atualizado_em = models.DateTimeField(auto_now=True)
    
