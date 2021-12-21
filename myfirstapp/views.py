from django.forms import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CarModel


class UserListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all().values()
        return Response(cars, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        car = CarModel.objects.create(**data)
        return Response(model_to_dict(car), status.HTTP_201_CREATED)


class UserRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = CarModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Car with id not found', status.HTTP_404_NOT_FOUND)

        car = CarModel.objects.get(pk=pk)
        return Response(model_to_dict(car), status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        exists = CarModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Car with id not found', status.HTTP_404_NOT_FOUND)
        CarModel.objects.filter(pk=pk).update(**data)

        return Response('car updated', status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = CarModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Car with id not found', status.HTTP_404_NOT_FOUND)

        car = CarModel.objects.filter(pk=pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
