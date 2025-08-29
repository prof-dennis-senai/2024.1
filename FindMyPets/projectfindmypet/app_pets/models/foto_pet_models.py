from django.db import models
from .pet_models import PetModels

# Create your models here.
class FotoPetModels(models.Model):
    pet = models.ForeignKey(PetModels, on_delete=models.CASCADE)
    caminho_imagem = models.ImageField(upload_to='fotos/%Y/%m/%d')
    descricao = models.TextField()
    principal = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)