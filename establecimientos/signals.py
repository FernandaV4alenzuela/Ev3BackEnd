from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from.models import Asignacion, Rol

# SIGNALS ESTABLECIMIENTOS

@receiver(m2m_changed, sender=Asignacion)
def asignar_rol_automático(sender, instance, action, **kwargs):
    if action == 'post_add':
        # Asigna un rol por defecto al usuario
        rol_default = Rol.objects.get_or_create(nombre='Empleado')[0]
        Asignacion.objects.create(usuario=instance.usuario, establecimiento=instance.establecimiento, rol=rol_default)