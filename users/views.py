from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView
from django.contrib.auth import get_user_model

from .serializers import UserSerializer

UserModel: User = get_user_model()


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
