# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qb', '0004_auto_20160113_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='passed',
            field=models.BooleanField(default=False),
        ),
    ]
