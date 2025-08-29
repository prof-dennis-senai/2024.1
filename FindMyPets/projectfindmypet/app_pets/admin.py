from django.contrib import admin
from .models import PetModels, FotoPetModels


# Register your models here.
@admin.register(PetModels)
class PetAdmin(admin.ModelAdmin):
    list_display = ('nome', 'raca', 'especie', 'sexo', 'porte', 'cor', 'status')
    search_fields = ('nome', 'raca', 'especie', 'status')
    list_filter = ('especie', 'sexo', 'porte', 'cor', 'status')

@admin.register(FotoPetModels)
class FotoPetAdmin(admin.ModelAdmin):
    list_display = ('pet', 'caminho_imagem', 'principal', 'criado_em')
    search_fields = ('pet',)