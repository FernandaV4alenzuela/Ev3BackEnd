from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # Formulario default de DJango para crear nuevos usuarios.
from django.contrib.auth import login # Funcion de Django para inicios de sesion.
from django.contrib.auth.models import User
from.forms import CustomUserCreationForm, UserProfileForm 
from django import forms
from django.contrib.auth.decorators import login_required

# Create your views here
# USUARIOS VIEWS


# View/ Funcion para crear los usuarios.
def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})




@login_required
def actualizar_user(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user.profile)  # Aqui se usa request.user.profile
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user.profile)  # Aqui tambien se usa request.user.profile
    return render(request, 'usuarios/actualizarUser.html', {'form': form})


