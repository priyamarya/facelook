# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0006_auto_20160510_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='card',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='user',
        ),
        migrations.AddField(
            model_name='cards',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]
