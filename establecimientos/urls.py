from django.urls import path
from. import views

# VIEWS ESTABLECIMIENTOS

urlpatterns = [
    path('crear/', views.crear_establecimiento, name='crear_establecimiento'),
    path('lista/', views.lista_establecimientos, name='lista_establecimientos'),
    path('actualizar/<pk>/', views.actualizar_establecimiento, name='actualizar_establecimiento'),
    path('eliminar/<pk>/', views.eliminar_establecimiento, name='eliminar_establecimiento'),
    path('<pk>/asignar_rol/', views.asignar_rol, name='asignar_rol'),
    path('<pk>/lista_asignaciones/', views.lista_asignaciones, name='lista_asignaciones'),
    path('asignacion/<pk_asignacion>/eliminar/', views.eliminar_asignacion, name='eliminar_asignacion'),
]