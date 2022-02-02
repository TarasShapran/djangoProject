from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from .models import ApartmentModel
from .serializers import ApartmentsSerializer


class ApartmentsListCreateView(ListCreateAPIView):
    serializer_class = ApartmentsSerializer
    queryset = ApartmentModel.objects.all()
    permission_classes = (AllowAny,)


class ApartmentRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = ApartmentsSerializer
    queryset = ApartmentModel.objects.all()
