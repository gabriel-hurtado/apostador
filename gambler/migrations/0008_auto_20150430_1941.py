# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gambler', '0007_auto_20150429_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apuesta',
            name='cuota',
            field=models.DecimalField(default=1, max_digits=3, decimal_places=2),
            preserve_default=True,
        ),
    ]
