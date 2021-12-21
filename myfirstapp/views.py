from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import DBtest


class UserListCreateView(APIView):
    def get(self, *args, **kwargs):
        users = DBtest.read_db()
        return Response(users, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        user = self.request.data
        new_user = DBtest.create(user)
        return Response(new_user, status.HTTP_201_CREATED)


class UserRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        users = DBtest.read_db()
        for user in users:
            if user.get('id') == pk:
                return Response(user, status.HTTP_200_OK)
        return Response('User with id not found', status.HTTP_404_NOT_FOUND)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        user = DBtest.update(data, pk)
        if not user:
            return Response('User with id not found', status.HTTP_404_NOT_FOUND)
        return Response(user, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        is_delete = DBtest.delete(pk)
        if not is_delete:
            return Response('User with id not found', status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
