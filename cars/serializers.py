from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from .models import CarModel


class CarSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'
        extra_kwargs = {
            'autopark': {'read_only': True}
        }

    def validate(self, data):
        if data.get('model' == data.get('brand')):
            raise serializers.ValidationError('Error model is equal brand')
        return data
