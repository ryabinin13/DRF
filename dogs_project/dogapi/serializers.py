from rest_framework import serializers
from .models import Dog


class DogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dog
        fields = '__all__'