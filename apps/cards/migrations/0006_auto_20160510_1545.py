# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('cards', '0005_cards_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'Likes',
                'verbose_name_plural': 'Likes',
            },
        ),
        migrations.RemoveField(
            model_name='cards',
            name='likes',
        ),
        migrations.AddField(
            model_name='likes',
            name='card',
            field=models.ForeignKey(to='cards.Cards'),
        ),
        migrations.AddField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(to='users.UserProfile'),
        ),
    ]
