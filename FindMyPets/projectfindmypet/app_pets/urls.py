from django.urls import path
from . import views
from .api import apis

from django.urls import path, include
from rest_framework import routers


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'pets', apis.PetsList)

urlpatterns = [
    path('', views.home, name='home'),
    path('pets/', views.listagem_pets, name='listagem_pets'),
    path('pets/cadastro/', views.cadastro_pets, name='cadastrar_pet'),
    path('pets/excluir/<int:id>', views.excluir_pet, name='excluir_pet'),
    path('pets/editar/<int:id>', views.editar_pet, name='editar_pet'),
    path('api/', include(router.urls)),
]
