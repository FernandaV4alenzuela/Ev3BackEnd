from django.urls import path
from. import views

# URLS RECETAS

urlpatterns = [
    path('crear/', views.crear_receta, name='crear_receta'),
    path('lista/', views.lista_recetas, name='lista_recetas'),
    path('actualizar/<pk>/', views.actualizar_receta, name='actualizar_receta'),
    path('eliminar/<pk>/', views.eliminar_receta, name='eliminar_receta'),
]