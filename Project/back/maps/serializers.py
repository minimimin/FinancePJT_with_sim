from rest_framework import serializers
from .models import Region

class RegionSerializer(serializers.Serializer):
    class Meta:
        model = Region
        fields = '__all__'