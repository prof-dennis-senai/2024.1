from rest_framework import serializers
from app_pets.models import PetModels

class PetsSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = PetModels