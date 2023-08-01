from datetime import datetime, timedelta

from apps.apartment.models import ApartmentModel
from apps.booking.models import BookingModel
from apps.booking.serializers import BookingSerializer
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from utils.booking_utils import BookingUtils


class BookingListView(ListAPIView):
    serializer_class = BookingSerializer
    queryset = BookingModel.objects.all()
    permission_classes = (IsAuthenticated,)


class BookingCreateView(GenericAPIView):
    serializer_class = BookingSerializer
    queryset = BookingModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        apartment_pk = kwargs.get('pk')
        check_in = datetime.strptime(self.request.data['check_in'], '%d-%m-%Y')
        check_out = datetime.strptime(self.request.data['check_out'], '%d-%m-%Y')
        reserved_apartments = BookingModel.objects.filter(apartment=apartment_pk, is_active=True)
        if reserved_apartments:
            BookingUtils.is_booking_date_free(reserved_apartments, check_in, check_out)
        user = self.request.user
        exists = ApartmentModel.objects.filter(pk=apartment_pk).exists()
        if not exists:
            return Response('Apartment not found ', status.HTTP_404_NOT_FOUND)
        apartment = ApartmentModel.objects.get(pk=apartment_pk)
        serializer = BookingSerializer(
            data={'booking_start': check_in, 'booking_end': check_out})
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user, apartment=apartment)
        return Response(serializer.data, status=status.HTTP_200_OK)
