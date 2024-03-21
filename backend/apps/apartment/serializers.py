from rest_framework.serializers import ModelSerializer

from .models import ApartmentModel


class ApartmentsSerializer(ModelSerializer):
    class Meta:
        model = ApartmentModel
        exclude = ('user',)
        extra_kwargs = {
            'star_rating': {'read_only': True},
        }
