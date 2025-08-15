from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PetViewSet, TutorViewSet

router = DefaultRouter()
router.register(r'pets', PetViewSet)
router.register(r'tutores', TutorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
