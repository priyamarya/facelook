# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0003_cards_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='v_type',
            field=models.CharField(default=b'public', max_length=125, choices=[(b'public', b'public'), (b'private', b'private')]),
        ),
    ]
