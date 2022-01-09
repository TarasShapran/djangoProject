from django.forms import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins

from .models import CarModel
from .serializers import CarSerializer


class CarsListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        year = self.request.query_params.get('year')
        qs = CarModel.objects.all()
        if year:
            qs = qs.filter(year__gte=year)
        return qs


class CarsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
