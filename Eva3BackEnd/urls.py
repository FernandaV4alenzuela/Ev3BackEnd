
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include("usuarios.urls")),
    path('recetas/', include("recetas.urls")),
    path('establecimientos/', include("establecimientos.urls")),
]
