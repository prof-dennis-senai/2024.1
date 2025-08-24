from django.db import models

# Create your models here.
class PetModels(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    especie = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    sexo = models.CharField(max_length=100)
    porte = models.CharField(max_length=100)
    cor = models.CharField(max_length=100)
    descricao = models.TextField()
    microchip_codigo = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'PetModels(nome ="{self.nome}", raca="{self.raca}")'
