from rest_framework import viewsets
from .models import Pet, Tutor
from .serializers import PetSerializer, TutorSerializer
from django.shortcuts import render

def home(request):
    return render(request, 'app_pets/pages/home.html')

class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
