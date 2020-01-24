# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d\xef\xbc\x88\xe6\x8c\x89\xe4\xbb\x8e\xe5\xa4\xa7\xe5\x88\xb0\xe5\xb0\x8f\xe6\x8e\x92\xe5\x88\x97\xef\xbc\x89')),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'db_table': 'Classification',
                'verbose_name_plural': '\u5206\u7c7b\uff08\u89c6\u9891\u5206\u7c7b\uff09',
            },
        ),
        migrations.CreateModel(
            name='Cooperation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d\xef\xbc\x88\xe6\x8c\x89\xe4\xbb\x8e\xe5\xa4\xa7\xe5\x88\xb0\xe5\xb0\x8f\xe6\x8e\x92\xe5\x88\x97\xef\xbc\x89')),
                ('href', models.CharField(default=b'javascript:void(0)', max_length=20, verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9a\xe8\xbf\x9e\xe6\x8e\xa5')),
                ('logo', models.ImageField(upload_to=b'./static/images/cooperation/', verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9aLOGO')),
                ('company', models.CharField(max_length=20, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'db_table': 'Cooperation',
                'verbose_name_plural': '\u4f01\u4e1a\u5408\u4f5c',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, '\u4e0b\u7ebf'), (1, '\u4e0a\u7ebf')])),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d')),
                ('icon', models.ImageField(upload_to=b'./static/images/icon/', null=True, verbose_name=b'\xe5\x9b\xbe\xe6\xa0\x87', blank=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0', db_index=True)),
                ('summary', models.CharField(default=b'summary', max_length=40, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b')),
            ],
            options={
                'db_table': 'Course',
                'verbose_name_plural': '\u8bfe\u7a0b',
            },
        ),
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d\xef\xbc\x88\xe6\x8c\x89\xe4\xbb\x8e\xe5\xa4\xa7\xe5\x88\xb0\xe5\xb0\x8f\xe6\x8e\x92\xe5\x88\x97\xef\xbc\x89')),
                ('name', models.CharField(max_length=32, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('classification', models.ManyToManyField(to='app01.Classification')),
            ],
            options={
                'db_table': 'Direction',
                'verbose_name_plural': '\u65b9\u5411\uff08\u89c6\u9891\u65b9\u5411\uff09',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.IntegerField(default=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x98\xbe\xe7\xa4\xba', choices=[(0, b'\xe4\xb8\x8d\xe6\x98\xbe\xe7\xa4\xba'), (1, b'\xe6\x98\xbe\xe7\xa4\xba')])),
                ('title', models.CharField(max_length=30, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('description', models.CharField(max_length=500, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b')),
                ('detail', models.TextField(null=True, verbose_name=b'\xe8\xaf\xa6\xe7\xbb\x86\xe5\x86\x85\xe5\xae\xb9', blank=True)),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d')),
            ],
            options={
                'ordering': ['-weight'],
                'verbose_name': '\u516c\u544a',
                'verbose_name_plural': '\u516c\u544a',
            },
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, '\u5df2\u8fc7\u671f'), (1, '\u62db\u8058\u4e2d')])),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d\xef\xbc\x88\xe6\x8c\x89\xe4\xbb\x8e\xe5\xa4\xa7\xe5\x88\xb0\xe5\xb0\x8f\xe6\x8e\x92\xe5\x88\x97\xef\xbc\x89')),
                ('title', models.CharField(max_length=20)),
                ('salary', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=20)),
                ('detail', models.TextField()),
                ('deadline', models.DateField()),
            ],
            options={
                'db_table': 'Recruit',
                'verbose_name_plural': '\u62db\u8058\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_active', models.IntegerField(default=1, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\x8a\xe7\xba\xbf', choices=[(1, b'\xe6\x98\xbe\xe7\xa4\xba'), (0, b'\xe4\xb8\x8d\xe6\x98\xbe\xe7\xa4\xba')])),
                ('name', models.CharField(unique=True, max_length=30, verbose_name=b'\xe6\xa0\x87\xe8\xaf\x86')),
                ('link', models.CharField(max_length=256, verbose_name=b'\xe9\x93\xbe\xe6\x8e\xa5')),
                ('img', models.ImageField(upload_to=b'./static/images/focus', verbose_name=b'\xe8\xbd\xae\xe6\x92\xad\xe5\x9b\xbe\xe7\x89\x87')),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d')),
                ('date_add', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe6\xb7\xbb\xe5\x8a\xa0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'ordering': ['-weight'],
                'verbose_name': '\u9996\u9875\u8f6e\u64ad',
                'verbose_name_plural': '\u9996\u9875\u8f6e\u64ad',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, '\u4e0b\u7ebf'), (1, '\u4e0a\u7ebf')])),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d\xef\xbc\x88\xe6\x8c\x89\xe4\xbb\x8e\xe5\xa4\xa7\xe5\x88\xb0\xe5\xb0\x8f\xe6\x8e\x92\xe5\x88\x97\xef\xbc\x89')),
                ('pic', models.ImageField(upload_to=b'./static/images/student_pic/', null=True, verbose_name=b'\xe5\xad\xa6\xe5\x91\x98\xe5\xa4\xb4\xe5\x83\x8f', blank=True)),
                ('name', models.CharField(unique=True, max_length=32, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0', db_index=True)),
                ('company', models.CharField(max_length=32, verbose_name=b'\xe5\xb0\xb1\xe4\xb8\x9a\xe5\x8d\x95\xe4\xbd\x8d')),
                ('salary', models.CharField(max_length=32, verbose_name=b'\xe8\x96\xaa\xe6\xb0\xb4')),
            ],
            options={
                'db_table': 'Student',
                'verbose_name_plural': '\u5b66\u751f\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d\xef\xbc\x88\xe6\x8c\x89\xe4\xbb\x8e\xe5\xa4\xa7\xe5\x88\xb0\xe5\xb0\x8f\xe6\x8e\x92\xe5\x88\x97\xef\xbc\x89')),
                ('letter_of_thanks', models.CharField(max_length=256, verbose_name=b'\xe5\xad\xa6\xe5\x91\x98\xe6\x84\x9f\xe8\xb0\xa2\xe4\xbf\xa1')),
                ('student', models.OneToOneField(to='app01.Student')),
            ],
            options={
                'db_table': 'StudentDetail',
                'verbose_name_plural': '\u5b66\u751f\u66f4\u591a\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, '\u4e0b\u7ebf'), (1, '\u4e0a\u7ebf')])),
                ('level', models.IntegerField(default=1, verbose_name=b'\xe7\xba\xa7\xe5\x88\xab', choices=[(1, '\u521d\u7ea7'), (2, '\u4e2d\u7ea7'), (3, '\u9ad8\u7ea7')])),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d\xef\xbc\x88\xe6\x8c\x89\xe4\xbb\x8e\xe5\xa4\xa7\xe5\x88\xb0\xe5\xb0\x8f\xe6\x8e\x92\xe5\x88\x97\xef\xbc\x89')),
                ('title', models.CharField(max_length=32, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('summary', models.CharField(max_length=32, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b')),
                ('img', models.ImageField(upload_to=b'./static/images/Video/', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
                ('href', models.CharField(max_length=256, verbose_name=b'\xe8\xa7\x86\xe9\xa2\x91\xe5\x9c\xb0\xe5\x9d\x80')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('classification', models.ForeignKey(blank=True, to='app01.Classification', null=True)),
            ],
            options={
                'db_table': 'Video',
                'verbose_name_plural': '\u89c6\u9891',
            },
        ),
    ]
