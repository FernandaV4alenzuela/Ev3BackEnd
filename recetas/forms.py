from django import forms
from.models import Receta

# FORMS RECETAS

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ('nombre', 'descripcion')