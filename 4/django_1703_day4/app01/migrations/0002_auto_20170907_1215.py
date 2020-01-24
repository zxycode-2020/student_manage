# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe7\x8f\xad\xe7\xba\xa7\xe5\x90\x8d')),
            ],
            options={
                'verbose_name': '\u73ed\u7ea7\u8868',
                'verbose_name_plural': '\u73ed\u7ea7\u8868',
            },
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': '\u5b66\u751f\u8868', 'verbose_name_plural': '\u5b66\u751f\u8868'},
        ),
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=18, verbose_name=b'\xe5\xad\xa6\xe7\x94\x9f\xe5\xb9\xb4\xe9\xbe\x84'),
        ),
        migrations.AddField(
            model_name='student',
            name='ip',
            field=models.GenericIPAddressField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=100, null=True, verbose_name=b'\xe5\xad\xa6\xe7\x94\x9f\xe9\x82\xae\xe7\xae\xb1', blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=30, verbose_name=b'\xe5\xad\xa6\xe7\x94\x9f\xe5\xa7\x93\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='student',
            name='score',
            field=models.DecimalField(null=True, verbose_name=b'\xe5\xad\xa6\xe7\x94\x9f\xe6\x88\x90\xe7\xbb\xa9', max_digits=5, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='cls',
            field=models.ForeignKey(default=1, to='app01.Class'),
            preserve_default=False,
        ),
    ]
