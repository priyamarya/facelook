# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0004_cards_v_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
