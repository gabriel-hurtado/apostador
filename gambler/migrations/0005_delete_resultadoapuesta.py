# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gambler', '0004_resultadoapuesta'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ResultadoApuesta',
        ),
    ]
