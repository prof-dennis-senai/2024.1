from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from app_pets.models import PetModels
from .serializers import PetsSerializers
from rest_framework import viewsets


# ViewSets define the view behavior.
class PetsList(viewsets.ModelViewSet):
    queryset = PetModels.objects.all()
    serializer_class = PetsSerializers