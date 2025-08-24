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
    if request.method == 'GET':
        return render(request, 'primeiroapp/pages/teste.html', {'produtos': lista_produtos})

    nome = request.POST.get('nome')
    preco = request.POST.get('preco')

    lista_produtos.append({
        "id": len(lista_produtos) + 1,
        "nome": nome,
        "preco": preco
    })

    return render(request, 'primeiroapp/pages/teste.html', {'produtos': lista_produtos})

def remover_item(request, id):
    print(id, lista_produtos.pop(id - 1))
    return render(request, 'primeiroapp/pages/teste.html', {'produtos': lista_produtos})


def atualizar_item(request, id):
    if request.method == 'GET':
        return render(request, 'primeiroapp/pages/atualizar.html', {'produtos': lista_produtos, "item_id":id})
    
    item = lista_produtos[id - 1]

    item['nome'] = request.POST.get('nome')
    item['preco'] = request.POST.get('preco')

    lista_produtos[id - 1] = item
    return render(request, 'primeiroapp/pages/teste.html', {'produtos': lista_produtos})