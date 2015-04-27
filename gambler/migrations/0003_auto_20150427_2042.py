# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gambler', '0002_auto_20150427_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='apuesta',
            name='resultado',
            field=models.ForeignKey(default=-1, to='gambler.Resultado'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='resultado',
            name='golLocal',
            field=models.IntegerField(default=-1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resultado',
            name='golVisitante',
            field=models.IntegerField(default=-1),
            preserve_default=True,
        ),
    ]
