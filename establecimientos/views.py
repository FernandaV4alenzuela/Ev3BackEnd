from django.shortcuts import render, redirect
from.forms import EstablecimientoForm, AsignacionForm
from.models import Establecimiento, Asignacion
from django.contrib.auth.decorators import login_required

# VIEWS ESTABLECIMIENTOS

@login_required
def crear_establecimiento(request):
    if request.method == 'POST':
        form = EstablecimientoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_establecimientos')
    else:
        form = EstablecimientoForm()
    return render(request, 'establecimientos/crear_establecimiento.html', {'form': form})

def lista_establecimientos(request):
    establecimientos = Establecimiento.objects.all()
    return render(request, 'establecimientos/lista_establecimientos.html', {'establecimientos': establecimientos})




@login_required
def actualizar_establecimiento(request, pk):
    establecimiento = Establecimiento.objects.get(pk=pk)
    if request.method == 'POST':
        form = EstablecimientoForm(request.POST, instance=establecimiento)
        if form.is_valid():
            form.save()
            return redirect('lista_establecimientos')
    else:
        form = EstablecimientoForm(instance=establecimiento)
    return render(request, 'establecimientos/actualizar_establecimiento.html', {'form': form})




@login_required
def eliminar_establecimiento(request, pk):
    establecimiento = Establecimiento.objects.get(pk=pk)
    if request.method == 'POST':
        establecimiento.delete()
        return redirect('lista_establecimientos')
    return render(request, 'establecimientos/eliminar_establecimiento.html', {'establecimiento': establecimiento})




@login_required
def asignar_rol(request, pk):
    establecimiento = Establecimiento.objects.get(pk=pk)
    if request.method == 'POST':
        form = AsignacionForm(request.POST)
        if form.is_valid():
            asignacion = form.save(commit=False)
            asignacion.establecimiento = establecimiento
            asignacion.save()
            return redirect('lista_asignaciones', pk=pk)
    else:
        form = AsignacionForm()
    return render(request, 'establecimientos/asignar_rol.html', {'form': form, 'establecimiento': establecimiento})

def lista_asignaciones(request, pk):
    establecimiento = Establecimiento.objects.get(pk=pk)
    asignaciones = Asignacion.objects.filter(establecimiento=establecimiento)
    return render(request, 'establecimientos/lista_asignaciones.html', {'asignaciones': asignaciones, 'establecimiento': establecimiento})




@login_required
def eliminar_asignacion(request, pk_asignacion):
    asignacion = Asignacion.objects.get(pk=pk_asignacion)
    if request.method == 'POST':
        asignacion.delete()
        return redirect('lista_asignaciones', pk=asignacion.establecimiento.pk)
    return render(request, 'establecimientos/eliminar_asignacion.html', {'asignacion': asignacion})