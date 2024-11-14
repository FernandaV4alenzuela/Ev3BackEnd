from django.urls import path
from. import views

# URLS USUARIOS
urlpatterns = [
    path('registro/', views.registro),
    path('actualizarUser/', views.actualizar_user),
    
]