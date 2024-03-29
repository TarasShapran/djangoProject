from datetime import timedelta

from django.contrib.auth import get_user_model

from backend.exceptions.jwt_exception import JwtException

from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework_simplejwt.tokens import BlacklistMixin, Token

UserModel = get_user_model()


class _ActionToken(BlacklistMixin, Token):
    lifetime = timedelta(hours=12)


class JwtUtils:
    def __init__(self, token_type: str, lifetime: dict = None, token_class=_ActionToken):
        self._TokenClass = token_class
        if lifetime:
            self._TokenClass.lifetime = timedelta(**lifetime)
        self._TokenClass.token_type = token_type

    def create_token(self, user):
        return self._TokenClass.for_user(user)

    def validate_token(self, token):
        try:
            action_token = self._TokenClass(token)
            if not OutstandingToken.objects.filter(token=token).exists():
                raise JwtException
            action_token.check_blacklist()
            action_token.blacklist()
            user_id = action_token.payload.get('user_id')
            return UserModel.objects.get(pk=user_id)
        except Exception:
            raise JwtException
