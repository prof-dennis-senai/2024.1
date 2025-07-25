from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')