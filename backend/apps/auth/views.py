from django.contrib.auth import get_user_model

from backend.enums.action_token import ActionTokenEnum
from backend.utils.email_utils import EmailUtils
from backend.utils.jwt_utils import JwtUtils
from rest_framework import status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import EmailSerializer

UserModel = get_user_model()


class ActivateView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        token = kwargs.get('token')
        user = JwtUtils(ActionTokenEnum.ACTIVATE.token_type).validate_token(token)
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)


class RecoverPasswordView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = EmailSerializer(data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data['email']
        user = get_object_or_404(UserModel, email)
        token = JwtUtils('recovery').create_token(user)
        EmailUtils.recovery_password_email(email, token, self.request)
        return Response(status=status.HTTP_200_OK)


class LogoutView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        user = self.request.user
        return Response(status=status.HTTP_200_OK)
