# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('score', models.DecimalField(max_digits=5, decimal_places=2)),
                ('email', models.EmailField(max_length=100)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
