from django.urls import reverse
from app_pets.models import PetModels
import pytest


@pytest.mark.django_db
def test_integracao_criar_pet(client):
    PetModels.objects.create(
        nome = 'Teste',
        data_nascimento = '2000-01-01',
        especie = 'Teste',
        raca = 'Teste',
        sexo = 'Teste',
        porte = 'Teste',
        cor = 'Teste',
        descricao = 'Teste',
        microchip_codigo = 'Teste',
        status = 'Teste',
    )

    response = client.get(reverse('listagem_pets'))
    assert response.status_code == 200
    assert len(response.context['pets']) == 1

    assert '<td>Teste</td>' in response.content.decode('utf-8')