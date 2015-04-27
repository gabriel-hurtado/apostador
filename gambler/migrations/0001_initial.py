# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apuesta',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('apuesta', models.DecimalField(max_digits=11, decimal_places=2)),
                ('cuota', models.DecimalField(max_digits=3, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('nombreEquipo', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('jornada', models.IntegerField()),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('golLocal', models.IntegerField()),
                ('golVisitante', models.IntegerField()),
                ('equipoLocal', models.ForeignKey(related_name='equipo_local', to='gambler.Equipo')),
                ('equipoVisitante', models.ForeignKey(related_name='equipo_visitante', to='gambler.Equipo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='apuesta',
            name='partido',
            field=models.ForeignKey(to='gambler.Partido'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='apuesta',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=True,
        ),
    ]
