# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qb', '0005_story_passed'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='checked',
            field=models.BooleanField(default=False),
        ),
    ]
