# Generated by Django 4.0 on 2022-02-03 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0003_alter_apartmentmodel_star_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentmodel',
            name='star_rating',
            field=models.IntegerField(default=0),
        ),
    ]
