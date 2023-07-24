from django.shortcuts import render, HttpResponseRedirect
from .models import Animal
# Create your views here.

def home(request):
    dados = {
        'dados': Animal.objects.all()
    }
    return render(request, 'home.html', dados)

def adicionar(request):
    return render(request, 'adicionar.html')

def add(request):
    animal = Animal()
    animal.cliente = request.POST['cliente']
    animal.animal = request.POST['animal']
    animal.idade = int(request.POST['idade'])
    animal.servico = request.POST['servico']
    animal.valor = float(request.POST['valor'])
    animal.pagamento = request.POST['pagamento']

    animal.save()
    
    return HttpResponseRedirect("/home")

def editar(request,ID):
    dado = {
        'dado': Animal.objects.get(id=ID)
    }
    return render(request, 'editar.html', dado)

def editSave(request):
    animal = Animal.objects.get(id=request.POST['id'])
    animal.cliente = request.POST['cliente']
    animal.animal = request.POST['animal']
    animal.idade = int(request.POST['idade'])
    animal.servico = request.POST['servico']
    animal.valor = float(request.POST['valor'])
    animal.pagamento = request.POST['pagamento']

    animal.save()

    return HttpResponseRedirect("/home")

def deletar(request,ID):
    Animal.objects.get(id=ID).delete()
    return HttpResponseRedirect("/home")

def goHome(request):
    return HttpResponseRedirect("/home")
