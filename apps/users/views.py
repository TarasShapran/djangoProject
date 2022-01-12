from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest_framework.generics import ListCreateAPIView

from .serializers import UserSerializer

UserModel: User = get_user_model()


class UserListView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
