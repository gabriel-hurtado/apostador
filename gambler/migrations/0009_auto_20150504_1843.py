# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gambler', '0008_auto_20150430_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apuesta',
            name='cuota',
        ),
        migrations.AddField(
            model_name='partido',
            name='cuota',
            field=models.DecimalField(max_digits=3, default=1, decimal_places=2),
            preserve_default=True,
        ),
    ]
