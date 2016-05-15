# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0008_cardlikes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardlikes',
            name='card',
        ),
        migrations.RemoveField(
            model_name='cardlikes',
            name='user',
        ),
        migrations.DeleteModel(
            name='CardLikes',
        ),
    ]
