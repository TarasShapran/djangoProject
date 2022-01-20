from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from utils.jwt_utils import JwtUtils


class ActivateView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        token = kwargs.get('token')
        user = JwtUtils.validate_token(token)
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)
