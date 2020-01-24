# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameOfThrone', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='score',
            field=models.DecimalField(decimal_places=2, default=99.99, max_digits=5, blank=True, null=True, verbose_name=b'\xe5\xad\xa6\xe7\x94\x9f\xe6\x88\x90\xe7\xbb\xa9'),
        ),
    ]
