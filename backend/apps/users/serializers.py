from django.contrib.auth import get_user_model

from backend.apps.apartment.serializers import ApartmentsSerializer
from backend.apps.profile.models import ProfileModel
from backend.apps.profile.serializers import ProfileSerializer
from backend.utils.email_utils import EmailUtils
from backend.utils.jwt_utils import JwtUtils
from rest_framework.serializers import ModelSerializer

from .models import UserModel as User

UserModel: User = get_user_model()


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()
    apartments = ApartmentsSerializer(many=True, read_only=True)

    class Meta:
        model = UserModel
        fields = (
            'id', 'email', 'password', 'is_active', 'is_staff', 'last_login', 'is_superuser', 'creates_at',
            'updated_at', 'profile', 'apartments')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data: dict):
        profile = validated_data.pop('profile')
        user = UserModel.objects.create_user(**validated_data)
        ProfileModel.objects.create(**profile, user=user)
        token = JwtUtils('activate', {'minutes': 30}).create_token(user)
        request = self.context.get('request')
        EmailUtils.register_email(user.email, profile.get('name'), token, request)
        return user
