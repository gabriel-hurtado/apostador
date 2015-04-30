# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gambler', '0005_delete_resultadoapuesta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('nombre', models.TextField()),
                ('password', models.TextField()),
                ('cuenta', models.DecimalField(max_digits=11, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='apuesta',
            name='user',
            field=models.ForeignKey(to='gambler.Usuario'),
            preserve_default=True,
        ),
    ]
