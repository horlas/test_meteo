from rest_framework import serializers
from .models import Peak

class PeaksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peak
        field = ['name', 'lat', 'lon', 'altitude']
