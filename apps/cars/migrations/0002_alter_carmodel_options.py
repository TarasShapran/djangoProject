# Generated by Django 4.0 on 2022-01-20 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carmodel',
            options={'ordering': ('id',), 'verbose_name': 'car', 'verbose_name_plural': 'cars'},
        ),
    ]