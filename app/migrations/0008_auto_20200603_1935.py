# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-03 16:35
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0007_auto_20200603_1920'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.FileField(default='temp.png', upload_to='', verbose_name='Путь к картинке'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 6, 3, 19, 35, 15, 29164), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2020, 6, 3, 19, 35, 15, 31165), verbose_name='Дата'),
        ),
    ]
