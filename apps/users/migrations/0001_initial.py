# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('about', models.TextField(null=True, blank=True)),
                ('joining_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(verbose_name=b'related to', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Users',
                'verbose_name_plural': ' Users',
            },
        ),
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=255, null=True, blank=True)),
                ('gender', models.CharField(max_length=125, choices=[(b'Others', b'Others'), (b'Male', b'Male'), (b'Female', b'Female')])),
                ('profile_pic', models.ImageField(null=True, upload_to=b'users', blank=True)),
                ('userlink', models.OneToOneField(verbose_name=b'of user', to='users.UserProfile')),
            ],
            options={
                'verbose_name': 'UsersInfo',
                'verbose_name_plural': 'UsersInfo',
            },
        ),
    ]
