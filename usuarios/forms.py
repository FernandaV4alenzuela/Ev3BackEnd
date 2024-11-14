from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.models import Profile

class CustomUserCreationForm(UserCreationForm):
    nombre = forms.CharField(max_length=100, required=True)
    apellido = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name ', 'last_name')
        
        
# Funcionalidad para modificar los usuarios. 
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username',)       