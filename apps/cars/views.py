from django.forms import model_to_dict

from apps.autopark.serializers import AutoParkSerializer
from rest_framework import mixins, status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CarModel
from .serializers import CarSerializer


class CarsListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (AllowAny,)

    def get_queryset(self):
        year = self.request.query_params.get('year')
        auto_park_id = self.request.query_params.get('autoParkId')
        qs = self.queryset.all()
        if year:
            qs = qs.filter(year__gte=year)
        if auto_park_id:
            qs = qs.filter(autopark_id=auto_park_id)
        return qs


class CarsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class CarsRetrieveAutoParkIdView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = AutoParkSerializer
