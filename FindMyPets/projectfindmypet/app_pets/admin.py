from django.contrib import admin
from .models import PetModels


# Register your models here.
@admin.register(PetModels)
class PetAdmin(admin.ModelAdmin):
    list_display = ('nome', 'raca', 'especie', 'sexo', 'porte', 'cor', 'status')
    search_fields = ('nome', 'raca', 'especie', 'status')
    list_filter = ('especie', 'sexo', 'porte', 'cor', 'status')
