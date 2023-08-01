# Generated by Django 4.0 on 2022-02-03 14:28

import datetime

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apartment', '0004_alter_apartmentmodel_star_rating'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_start', models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2022, 2, 3, 16, 28, 28, 846868))])),
                ('booking_end', models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2022, 2, 3, 16, 28, 28, 846868)), django.core.validators.MinValueValidator(models.DateTimeField(validators=[django.core.validators.MinValueValidator(datetime.datetime(2022, 2, 3, 16, 28, 28, 846868))]))])),
                ('price', models.IntegerField()),
                ('isActive', models.BooleanField()),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apartment.apartmentmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='users.usermodel')),
            ],
            options={
                'db_table': 'bookings',
            },
        ),
    ]