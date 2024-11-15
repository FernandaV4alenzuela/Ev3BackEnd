from django.shortcuts import render, redirect
from.forms import RecetaForm
from.models import Receta
from django.contrib.auth.decorators import login_required

# VIEWS RECETAS

@login_required
def crear_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_recetas')
    else:
        form = RecetaForm()
    return render(request, 'recetas/crear_receta.html', {'form': form})

def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'recetas/lista_recetas.html', {'recetas': recetas})




@login_required
def actualizar_receta(request, pk):
    receta = Receta.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecetaForm(request.POST, instance=receta)
        if form.is_valid():
            form.save()
            return redirect('lista_recetas')
    else:
        form = RecetaForm(instance=receta)
    return render(request, 'recetas/actualizar_receta.html', {'form': form})




@login_required
def eliminar_receta(request, pk):
    receta = Receta.objects.get(pk=pk)
    if request.method == 'POST':
        receta.delete()
        return redirect('lista_recetas')
    return render(request, 'recetas/eliminar_receta.html', {'receta': receta})