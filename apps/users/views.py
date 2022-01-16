from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from apps.profile.serializers import AvatarSerializer
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .permissions import IsSuperUser
from .serializers import UserSerializer

UserModel: User = get_user_model()


class UserListView(ListCreateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    # queryset = UserModel.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST':
            return AllowAny(),
        return IsAuthenticated(),


class UserToAdminView(GenericAPIView):
    permission_classes = (IsSuperUser,)
    queryset = UserModel.objects.all()

    def patch(self, *args, **kwargs):
        user = self.get_object()
        UserModel.objects.to_admin(user)
        data = UserSerializer(user).data
        return Response(data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        user = self.get_object()
        UserModel.objects.to_user(user)
        data = UserSerializer(user).data
        return Response(data, status.HTTP_200_OK)


class AddAvatarView(GenericAPIView):
    def patch(self, *args, **kwargs):
        avatar_data = self.request.FILES.get('avatar')
        serializer = AvatarSerializer(data={'url': avatar_data})
        serializer.is_valid(raise_exception=True)
        serializer.save(profile=self.request.user.profile)
        user = UserSerializer(self.request.user).data
        return Response(user, status.HTTP_200_OK)
