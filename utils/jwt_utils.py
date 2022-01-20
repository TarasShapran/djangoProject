from datetime import timedelta

from django.contrib.auth import get_user_model

from exceptions.jwt_exception import JwtException

from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework_simplejwt.tokens import AccessToken, BlacklistMixin

UserModel = get_user_model()


class _AccessToken(BlacklistMixin, AccessToken):
    token_type = 'action'
    lifetime = timedelta(minutes=30)


class JwtUtils:
    @staticmethod
    def create_token(user):
        return _AccessToken.for_user(user)

    @staticmethod
    def validate_token(token):
        try:
            action_token = _AccessToken(token)
            if not OutstandingToken.objects.filter(token=token).exists():
                raise JwtException
            action_token.check_blacklist()
            action_token.blacklist()
            user_id = action_token.payload.get('user_id')
            return UserModel.objects.get(pk=user_id)
        except Exception:
            raise JwtException
