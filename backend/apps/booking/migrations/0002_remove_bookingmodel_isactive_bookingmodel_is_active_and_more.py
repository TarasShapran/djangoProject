# Generated by Django 4.0 on 2022-02-04 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookingmodel',
            name='isActive',
        ),
        migrations.AddField(
            model_name='bookingmodel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='bookingmodel',
            name='booking_end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='bookingmodel',
            name='booking_start',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='bookingmodel',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
