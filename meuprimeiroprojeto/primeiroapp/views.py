from django.shortcuts import render

lista_produtos = [
    {
        'id': 1,
        'nome': 'Camisa',
        'preco': 100
    }
]

# Create your views here.
def home(request):
    return render(request, 'primeiroapp/pages/home.html', context={'lista_num': [1,2,3,4,5,6]})

def sobre(request):
    return render(request, 'primeiroapp/pages/sobre.html')

def teste(request):
    return render(request, 'primeiroapp/pages/teste.html', {'produtos': lista_produtos})