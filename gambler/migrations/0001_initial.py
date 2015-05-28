# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Apuesta',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('apuesta', models.DecimalField(decimal_places=2, max_digits=11)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('nombreEquipo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('jornada', models.IntegerField()),
                ('cuota', models.DecimalField(decimal_places=2, max_digits=3, default=1)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('equipoLocal', models.ForeignKey(related_name='equipo_local', to='gambler.Equipo')),
                ('equipoVisitante', models.ForeignKey(related_name='equipo_visitante', to='gambler.Equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('golLocal', models.IntegerField(default=-1)),
                ('golVisitante', models.IntegerField(default=-1)),
            ],
        ),
        migrations.AddField(
            model_name='partido',
            name='resultado',
            field=models.ForeignKey(to='gambler.Resultado'),
        ),
        migrations.AddField(
            model_name='apuesta',
            name='partido',
            field=models.ForeignKey(related_name='apuestas', to='gambler.Partido'),
        ),
        migrations.AddField(
            model_name='apuesta',
            name='resultado',
            field=models.ForeignKey(to='gambler.Resultado'),
        ),
        migrations.AddField(
            model_name='apuesta',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
