from django.shortcuts import render
from .models import IMC


def bonito(request):
    resultado = None
    if request.method == "POST":
        nome = request.POST.get('nome')
        peso = float(request.POST.get('peso'))
        altura = float(request.POST.get('altura'))

        nova_pessoa = IMC(nome=nome, peso=peso, altura=altura)
        nova_pessoa.calcular_imc()
        nova_pessoa.save()

        resultado = nova_pessoa.imc

    return render(request, 'bonito.html', {'resultado': resultado})

def index(request):
    return render(request, 'index.html')


