from datetime import datetime

from django.core import validators as V
from django.db import models

from apps.apartment.models import ApartmentModel
from apps.users.models import UserModel


class BookingModel(models.Model):
    class Meta:
        db_table = 'bookings'
        ordering: ('id',)

    booking_start = models.DateTimeField()
    booking_end = models.DateTimeField()
    price = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='bookings')
    apartment = models.ForeignKey(ApartmentModel, on_delete=models.CASCADE)
