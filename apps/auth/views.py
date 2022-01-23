from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from utils.email_utils import EmailUtils
from utils.jwt_utils import JwtUtils

from .serializers import EmailSerializer, PasswordSerializer

UserModel = get_user_model()


class ActivateView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        token = kwargs.get('token')
        user = JwtUtils('activate').validate_token(token)
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)


class RecoverPasswordView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = EmailSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']
        user = get_object_or_404(UserModel, email=email)
        token = JwtUtils('recovery', {'minutes': 30}).create_token(user)
        EmailUtils.recovery_password_email(email, token, self.request)
        return Response(status=status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        data = self.request.data
        token = data['token']
        serializer = PasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        password = serializer.data.get('password')
        user: User = JwtUtils('recovery').validate_token(token)
        user.set_password(password)
        user.save()
        return Response(status=status.HTTP_200_OK)
