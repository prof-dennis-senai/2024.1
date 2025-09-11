from django.db import models
import datetime

# Create your models here.
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
    
    def __str__(self):
        return self.username
    

class TokenSenha(models.Model):
    user = models.IntegerField()
    token = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    expirado_em = models.DateTimeField()

    @property
    def is_expired(self):
        return self.expirado_em.date() > datetime.datetime.now().date()