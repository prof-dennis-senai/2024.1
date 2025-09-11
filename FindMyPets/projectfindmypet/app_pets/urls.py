from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pets/', views.listagem_pets, name='listagem_pets'),
    path('pets/cadastro/', views.cadastro_pets, name='cadastrar_pet'),
    path('pets/excluir/<int:id>', views.excluir_pet, name='excluir_pet'),
    path('pets/editar/<int:id>', views.editar_pet, name='editar_pet')
]
