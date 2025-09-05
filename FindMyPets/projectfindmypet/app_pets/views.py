from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect


@login_required
def home(request):
    return render(request, 'app_pets/pages/home.html')

def login_in_app(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(home)

    return render(request, 'app_pets/pages/login.html')

def logout_in_app(request):
    logout(request)
    return redirect(home)