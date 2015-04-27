# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gambler', '0003_auto_20150427_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultadoApuesta',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('golLocal', models.IntegerField(default=-1)),
                ('golVisitante', models.IntegerField(default=-1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
