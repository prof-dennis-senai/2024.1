# projectfindmypet/urls.py
from django.contrib import admin
from django.urls import path, include
from app_pets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('api/', include('app_pets.urls')),  # <- ESSENCIAL
]
