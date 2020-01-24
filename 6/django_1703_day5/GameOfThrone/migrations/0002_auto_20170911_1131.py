# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('GameOfThrone', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nick', models.CharField(max_length=b'30', verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0')),
                ('qq', models.CharField(max_length=b'15', verbose_name=b'QQ')),
                ('phone', models.CharField(max_length=b'11', verbose_name=b'\xe7\x94\xb5\xe8\xaf\x9d')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u7528\u6237\u8be6\u7ec6\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u8be6\u7ec6\u4fe1\u606f',
            },
        ),
        migrations.AlterField(
            model_name='student',
            name='score',
            field=models.DecimalField(decimal_places=2, default=99.99, max_digits=5, blank=True, null=True, verbose_name=b'\xe5\xad\xa6\xe7\x94\x9f\xe6\x88\x90\xe7\xbb\xa9'),
        ),
    ]
