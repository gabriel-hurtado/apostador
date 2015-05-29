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
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('apuesta', models.DecimalField(decimal_places=2, max_digits=11)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nombreEquipo', models.TextField()),
                ('pais', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('jornada', models.IntegerField()),
                ('cuota', models.DecimalField(default=1, decimal_places=2, max_digits=3)),
                ('fecha', models.DateField(default=datetime.date.today)),
                ('equipoLocal', models.ForeignKey(to='gambler.Equipo', related_name='equipo_local')),
                ('equipoVisitante', models.ForeignKey(to='gambler.Equipo', related_name='equipo_visitante')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('golLocal', models.IntegerField(default=-1)),
                ('golVisitante', models.IntegerField(default=-1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='partido',
            name='resultado',
            field=models.ForeignKey(to='gambler.Resultado'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='apuesta',
            name='partido',
            field=models.ForeignKey(to='gambler.Partido', related_name='apuestas'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='apuesta',
            name='resultado',
            field=models.ForeignKey(to='gambler.Resultado'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='apuesta',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
