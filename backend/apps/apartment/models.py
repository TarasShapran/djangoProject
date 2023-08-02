from django.core import validators as V
from django.db import models

from backend.apps.users.models import UserModel


class ApartmentModel(models.Model):
    class Meta:
        db_table = 'apartments'
        ordering = ('id',)

    country = models.CharField(
        max_length=20,
        validators=[
            V.MinLengthValidator(3),
            V.MaxLengthValidator(20)
        ])
    city = models.CharField(
        max_length=20,
        validators=[
            V.MinLengthValidator(3),
            V.MaxLengthValidator(20)
        ])
    region = models.CharField(
        max_length=20,
        validators=[
            V.MinLengthValidator(3),
            V.MaxLengthValidator(20)
        ])
    number_of_rooms = models.IntegerField(
        validators=[
            V.MinValueValidator(1),
            V.MaxValueValidator(10)
        ])
    number_of_beds = models.IntegerField()
    amount_of_places = models.IntegerField()
    star_rating = models.IntegerField(default=0)
    description = models.CharField(
        max_length=500,
        validators=[
            V.MinLengthValidator(10),
            V.MaxLengthValidator(500)
        ])
    approve = models.BooleanField()
    price = models.IntegerField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='apartments')
