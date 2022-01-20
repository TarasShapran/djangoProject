# Generated by Django 4.0 on 2022-01-16 13:12

import django.db.models.deletion
from django.db import migrations, models

import utils.avatar_utils


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_profilemodel_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='avatar',
        ),
        migrations.CreateModel(
            name='AvatarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.ImageField(upload_to=utils.avatar_utils.AvatarUtils.upload_to)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avatars', to='profile.profilemodel')),
            ],
            options={
                'db_table': 'avatars',
            },
        ),
    ]