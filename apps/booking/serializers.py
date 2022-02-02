from apps.booking.models import BookingModel
from rest_framework.serializers import ModelSerializer


class BookingSerializer(ModelSerializer):
    class Meta:
        model = BookingModel
        exclude = ('user', 'apartment')
        extra_kwargs = {
            'price': {'read_only': True},
            'isActive': {'read_only': True}
        }
