# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-15 08:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 7, 15, 8, 51, 34, 432000, tzinfo=utc)),
        ),
    ]
