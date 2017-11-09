from rest_framework import serializers
from .models import Semilla, SemillaPersona


class SemillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semilla
        fields = ('pk','nombre', 'activo', 'version', 'updated', 'updated_by')

