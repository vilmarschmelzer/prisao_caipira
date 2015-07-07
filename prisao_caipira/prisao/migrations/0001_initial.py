# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prisioneiros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prisioneiro_id', models.IntegerField()),
                ('is_preso', models.BooleanField(default=True)),
                ('data', models.DateTimeField()),
            ],
        ),
    ]
