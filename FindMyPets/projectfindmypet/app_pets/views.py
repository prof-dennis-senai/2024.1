from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect


@login_required
def home(request):
    return render(request, 'app_pets/pages/home.html')