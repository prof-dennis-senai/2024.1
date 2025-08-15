from django.db import models

class Tutor(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Pet(models.Model):
    STATUS_CHOICES = (
        ('perdido', 'Perdido'),
        ('encontrado', 'Encontrado'),
        ('em_casa', 'Em casa'),
    )
    nome = models.CharField(max_length=100)
    especie = models.CharField(max_length=50)
    raca = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE, related_name='pets')

    def __str__(self):
        return self.nome

class Solicitacao(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='solicitacoes')
    mensagem = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitação para {self.pet.nome} em {self.data_criacao}"
