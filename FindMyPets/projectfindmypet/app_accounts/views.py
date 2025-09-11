from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from app_pets.views import home
from .models import CustomUser, TokenSenha
# Create your views here.

def login_in_app(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(home)

    return render(request, 'app_accounts/pages/login.html')

def logout_in_app(request):
    logout(request)
    return redirect(home)

def register(request):
    return render(request, 'app_pets/pages/register.html')

def password_reset(request, email=None, token=None):
    if request.method == 'POST':
        email = request.POST.get('email')
        validar_token = request.POST.get('token')
        nova_senha = request.POST.get('senha')

        token_obj = TokenSenha.objects.filter(token=validar_token).first()
        if token_obj and token_obj.is_expired:
            user = CustomUser.objects.filter(email=email).first()
            user.set_password(nova_senha)
            user.save()
            return redirect(home)

        return redirect(login_in_app)

    token_obj = TokenSenha.objects.filter(email=email).first()
    return render(request, 'app_pets/pages/password_reset.html', {'email': email, 'token': token_obj.token if token_obj else None})

def validar_usuario_alterar_senha(resquest):
    if resquest.user.forcar_alterar_senha:
        return redirect(password_reset, email=resquest.user.email)