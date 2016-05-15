# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('cards', '0007_auto_20160510_1547'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardLikes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('likes_like', models.IntegerField(default=0)),
                ('card', models.ForeignKey(to='cards.Cards')),
                ('user', models.ForeignKey(to='users.UserProfile')),
            ],
            options={
                'verbose_name': 'Likes',
                'verbose_name_plural': 'Likes',
            },
        ),
    ]
