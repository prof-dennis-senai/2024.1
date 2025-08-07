from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'primeiroapp/pages/home.html', context={'lista_num': [1,2,3,4,5,6]})

def sobre(request):
    return render(request, 'primeiroapp/pages/sobre.html')