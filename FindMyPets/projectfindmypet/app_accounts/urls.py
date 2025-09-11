from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_in_app, name='login'),
    path('logout/', views.logout_in_app, name='logout'),
    path('register/', views.register, name='register'),
    path('password_reset/', views.password_reset, name='password_reset')
]
