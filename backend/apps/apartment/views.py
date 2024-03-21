from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from .models import ApartmentModel
from .serializers import ApartmentsSerializer


class ApartmentsListView(ListAPIView):
    serializer_class = ApartmentsSerializer
    queryset = ApartmentModel.objects.all()
    permission_classes = (AllowAny,)


# @method_decorator(name='post', decorator=swagger_auto_schema(operation_id='List of Appartment'))
class ApartmentsCreateView(ListAPIView, GenericAPIView):
    """
    post:
        Create Apartments
    """
    serializer_class = ApartmentsSerializer
    queryset = ApartmentModel.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, *args, **kwargs):
        serializer = ApartmentsSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        apartment = serializer.data
        return Response(apartment, status=status.HTTP_200_OK)


class ApartmentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView, GenericAPIView):
    serializer_class = ApartmentsSerializer
    queryset = ApartmentModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        user = self.request.user
        exists = ApartmentModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Apartment not found ', status.HTTP_404_NOT_FOUND)
        is_access = ApartmentModel.objects.filter(pk=pk, user=user).exists()
        if not is_access:
            return Response('Access denied', status.HTTP_401_UNAUTHORIZED)
        apartment = ApartmentModel.objects.get(pk=pk)
        serializer = ApartmentsSerializer(instance=apartment, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def delete(self, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     user = self.request.user
    #     exists = ApartmentModel.objects.filter(pk=pk).exists()
    #     if not exists:
    #         return Response('Apartment not found ', status.HTTP_404_NOT_FOUND)
    #     is_access = ApartmentModel.objects.filter(pk=pk, user=user).exists()
    #     if not is_access:
    #         return Response('Access denied', status.HTTP_401_UNAUTHORIZED)
    #     ApartmentModel.objects.filter(pk=pk).delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
