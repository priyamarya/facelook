# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('cards', '0002_auto_20160508_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='cards',
            name='user',
            field=models.ForeignKey(default=b'', blank=True, to='users.UserProfile', null=True),
        ),
    ]
