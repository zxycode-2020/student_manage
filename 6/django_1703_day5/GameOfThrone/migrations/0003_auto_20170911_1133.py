# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GameOfThrone', '0002_auto_20170911_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=b'11', null=True, verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='qq',
            field=models.CharField(max_length=b'15', null=True, verbose_name=b'QQ', blank=True),
        ),
    ]
