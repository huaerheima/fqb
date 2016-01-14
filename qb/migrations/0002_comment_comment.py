# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qb', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.CharField(default=datetime.datetime(2016, 1, 13, 5, 49, 13, 431070, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
    ]
