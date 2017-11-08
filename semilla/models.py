from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Semilla(models.Model):

    nombre = models.CharField(max_length=30, blank=False, null=False)
    activo = models.BooleanField(default=True)
    version = models.IntegerField(default=1, blank=False, null=False)
    updated = models.DateTimeField(default=timezone.now(), blank=False, null=False)
    updated_by = models.ForeignKey(User, related_name="semilla_user")

    def __str__(self):
        return self.nombre


class SemillaPersona(models.Model):

    fk_semilla = models.ForeignKey(Semilla, related_name="semilla_per_semilla")
    fk_user = models.ForeignKey(User, related_name="semilla_per_user")
    imagen = models.ImageField(blank=False, null=True)
    disponible = models.BooleanField(default=True)
    updated = models.DateTimeField(default=timezone.now(), blank=False, null=False)