import pytest
from django.urls import reverse
from app_accounts.models import CustomUser

def test_rota_retorna_home():
    url = reverse('home')
    assert url == '/'


def test_rota_home_status_302_deslogado(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 302

@pytest.mark.slow 
@pytest.mark.django_db
def test_rota_home_status_200_logado(client):
    CustomUser.objects.create_user(username='admin', password='admin')
    
    client.login(username='admin', password='admin')

    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200


