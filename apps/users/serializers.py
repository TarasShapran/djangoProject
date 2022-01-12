from django.contrib.auth import get_user_model

from apps.profile.models import ProfileModel
from apps.profile.serializers import ProfileSerializer
from rest_framework.serializers import ModelSerializer

from .models import UserModel as User

UserModel: User = get_user_model()


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_staff', 'last_login', 'is_superuser', 'creates_at',
            'updated_at', 'profile')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        return user
