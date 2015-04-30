# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gambler', '0006_auto_20150428_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='password',
            new_name='contrasena',
        ),
    ]
