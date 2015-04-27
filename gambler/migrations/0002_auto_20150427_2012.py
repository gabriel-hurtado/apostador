# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gambler', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('golLocal', models.IntegerField(default=0)),
                ('golVisitante', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='partido',
            name='golLocal',
        ),
        migrations.RemoveField(
            model_name='partido',
            name='golVisitante',
        ),
        migrations.AddField(
            model_name='partido',
            name='resultado',
            field=models.ForeignKey(to='gambler.Resultado', default=0),
            preserve_default=False,
        ),
    ]
