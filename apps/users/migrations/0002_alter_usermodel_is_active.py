# Generated by Django 4.0 on 2022-01-20 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
