from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from .models import PetModels

from utils.send_email_utils.send_email_utils import enviar_email_cadastro_bem_vindo

@login_required
def home(request):
    enviar_email_cadastro_bem_vindo("seu_email@gmail.com", "João")
    return render(request, 'app_pets/pages/home.html')

def listagem_pets(request):
    search = request.GET.get('search')
    if search:
        pets = PetModels.objects.filter(name__icontains=search)

    else:
        pets = PetModels.objects.all()
    
    return render(request, 'app_pets/pages/listagem_pets.html', {'pets': pets})
    

def cadastro_pets(request):
    if request.method == 'POST':
        manter_cadastro = request.POST.get('manter_cadastro')
        print('>>>>>>>>>>>>', manter_cadastro)
        pet = PetModels(
            nome = request.POST.get('nome'),
            data_nascimento = request.POST.get('data_nascimento'),
            especie = request.POST.get('especie'),
            raca = request.POST.get('raca'),
            sexo = request.POST.get('sexo'),
            porte = request.POST.get('porte'),
            cor = request.POST.get('cor'),
            descricao = request.POST.get('descricao'),
            microchip_codigo = request.POST.get('microchip_codigo'),
            status = request.POST.get('status'),
        )
        pet.save()

        if manter_cadastro == 'on':
            return render(request, 'app_pets/pages/cadastro_pets.html', {'manter_cadastro': manter_cadastro})

        return redirect(listagem_pets)
        
    return render(request, 'app_pets/pages/cadastro_pets.html')

def editar_pet(request, id):
    pet = PetModels.objects.get(id=id)

    if request.method == 'POST':
        pet.nome = request.POST.get('nome')
        pet.data_nascimento = request.POST.get('data_nascimento')
        pet.especie = request.POST.get('especie')
        pet.raca = request.POST.get('raca')
        pet.sexo = request.POST.get('sexo')
        pet.porte = request.POST.get('porte')
        pet.cor = request.POST.get('cor')
        pet.descricao = request.POST.get('descricao')
        pet.microchip_codigo = request.POST.get('microchip_codigo')
        pet.status = request.POST.get('status')
        pet.save()

        return redirect(listagem_pets)

    return render(request, 'app_pets/pages/atualizar_pet.html', {'pet': pet})

def excluir_pet(request, id):
    pet = PetModels.objects.get(id=id)
    pet.delete()
    return redirect(listagem_pets)