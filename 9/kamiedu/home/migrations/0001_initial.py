# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(0, b'\xe4\xb8\x8b\xe7\xba\xbf'), (1, b'\xe4\xb8\x8a\xe7\xba\xbf')])),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d\xef\xbc\x9a\xe4\xbb\x8e\xe5\xa4\xa7\xe5\x88\xb0\xe5\xb0\x8f')),
                ('img', models.ImageField(upload_to=b'banner/', verbose_name=b'banner\xe5\x9b\xbe\xe7\x89\x87')),
                ('href', models.CharField(max_length=300, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87\xe9\x93\xbe\xe6\x8e\xa5')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u9996\u9875Banner',
                'verbose_name_plural': '\u9996\u9875Banner',
            },
        ),
        migrations.CreateModel(
            name='Cooperation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=b'100', verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x90\x8d\xe7\xa7\xb0')),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d\xe4\xbb\x8e\xe6\x89\x93\xe5\x88\xb0\xe5\xb0\x8f')),
                ('logo', models.ImageField(upload_to=b'logos/', verbose_name=b'\xe4\xbc\x81\xe4\xb8\x9alogo')),
                ('link', models.CharField(max_length=b'300', verbose_name=b'\xe9\x93\xbe\xe6\x8e\xa5\xe5\x9c\xb0\xe5\x9d\x80')),
            ],
            options={
                'verbose_name': '\u5408\u4f5c\u4f01\u4e1a',
                'verbose_name_plural': '\u5408\u4f5c\u4f01\u4e1a',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\x8a\xe7\xba\xbf', choices=[(0, b'\xe4\xb8\x8b\xe7\xba\xbf'), (1, b'\xe4\xb8\x8a\xe7\xba\xbf')])),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d\xef\xbc\x9a\xe4\xbb\x8e\xe5\xa4\xa7\xe5\x88\xb0\xe5\xb0\x8f')),
                ('name', models.CharField(max_length=b'30', verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe5\x90\x8d\xe7\xa7\xb0')),
                ('description', models.CharField(max_length=200, verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe7\xae\x80\xe4\xbb\x8b')),
                ('image', models.ImageField(upload_to=b'course/', verbose_name=b'\xe8\xaf\xbe\xe7\xa8\x8b\xe5\xb0\x81\xe9\x9d\xa2')),
            ],
            options={
                'verbose_name': '\u8bfe\u7a0b\u4ecb\u7ecd\u8868',
                'verbose_name_plural': '\u8bfe\u7a0b\u4ecb\u7ecd\u8868',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, verbose_name=b'\xe5\x85\xac\xe5\x91\x8a\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\x8a\xe7\xba\xbf', choices=[(0, b'\xe4\xb8\x8b\xe7\xba\xbf'), (1, b'\xe4\xb8\x8a\xe7\xba\xbf')])),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d\xef\xbc\x9a\xe4\xbb\x8e\xe5\xa4\xa7\xe5\x88\xb0\xe5\xb0\x8f')),
                ('title', models.CharField(max_length=50, verbose_name=b'\xe5\x85\xac\xe5\x91\x8a\xe6\xa0\x87\xe9\xa2\x98')),
                ('description', models.CharField(max_length=100, verbose_name=b'\xe5\x85\xac\xe5\x91\x8a\xe7\xae\x80\xe4\xbb\x8b')),
                ('content', models.TextField(verbose_name=b'\xe5\x85\xac\xe5\x91\x8a\xe5\x86\x85\xe5\xae\xb9')),
            ],
            options={
                'verbose_name': '\u4f01\u4e1a\u516c\u544a',
                'verbose_name_plural': '\u4f01\u4e1a\u516c\u544a',
            },
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, verbose_name=b'\xe6\x8b\x9b\xe8\x81\x98\xe6\x98\xaf\xe5\x90\xa6\xe4\xb8\x8a\xe7\xba\xbf', choices=[(0, b'\xe4\xb8\x8b\xe7\xba\xbf'), (1, b'\xe4\xb8\x8a\xe7\xba\xbf')])),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d\xef\xbc\x9a\xe4\xbb\x8e\xe5\xa4\xa7\xe5\x88\xb0\xe5\xb0\x8f')),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('company', models.CharField(max_length=200, verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8')),
                ('salary', models.CharField(max_length=30, verbose_name=b'\xe8\x96\xaa\xe6\xb0\xb4')),
                ('content', models.TextField(verbose_name=b'\xe8\xaf\xa6\xe6\x83\x85')),
                ('date_dead', models.DateTimeField()),
            ],
            options={
                'verbose_name': '\u62db\u8058\u4fe1\u606f',
                'verbose_name_plural': '\u62db\u8058\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status', models.IntegerField(default=1, verbose_name=b'\xe5\xad\xa6\xe7\x94\x9f\xe6\x98\xaf\xe5\x90\xa6\xe5\xb1\x95\xe7\xa4\xba', choices=[(0, b'\xe4\xb8\x8d\xe5\xb1\x95\xe7\xa4\xba'), (1, b'\xe5\xb1\x95\xe7\xa4\xba')])),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d\xef\xbc\x9a\xe4\xbb\x8e\xe5\xa4\xa7\xe5\x88\xb0\xe5\xb0\x8f')),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d')),
                ('avatar', models.ImageField(upload_to=b'avatar/', verbose_name=b'\xe7\x85\xa7\xe7\x89\x87')),
                ('company', models.CharField(max_length=100, verbose_name=b'\xe5\xb0\xb1\xe4\xb8\x9a\xe5\x85\xac\xe5\x8f\xb8')),
                ('salary', models.CharField(max_length=30, verbose_name=b'\xe5\xb0\xb1\xe4\xb8\x9a\xe8\x96\xaa\xe8\xb5\x84')),
            ],
            options={
                'verbose_name': '\u5b66\u751f\u8868',
                'verbose_name_plural': '\u5b66\u751f\u8868',
            },
        ),
        migrations.CreateModel(
            name='StuDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.IntegerField(default=0, verbose_name=b'\xe6\x9d\x83\xe9\x87\x8d,\xe4\xbb\x8e\xe5\xa4\xa7\xe5\x88\xb0\xe5\xb0\x8f')),
                ('letter', models.TextField(verbose_name=b'\xe6\x84\x9f\xe8\xb0\xa2\xe4\xbf\xa1')),
                ('student', models.OneToOneField(to='home.Student')),
            ],
            options={
                'verbose_name': '\u5b66\u751f\u8be6\u60c5\u8868',
                'verbose_name_plural': '\u5b66\u751f\u8be6\u60c5\u8868',
            },
        ),
    ]
