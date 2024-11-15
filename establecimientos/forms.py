from django import forms
from.models import Establecimiento, Asignacion

# FORMS ESTABLECIMIENTOS

class EstablecimientoForm(forms.ModelForm):
    class Meta:
        model = Establecimiento
        fields = ('nombre', 'descripcion')

class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = ('usuario', 'rol')