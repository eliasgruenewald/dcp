# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-09 09:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dcp', '0015_auto_20160709_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 9, 9, 49, 46, 827849, tzinfo=utc), verbose_name='date published'),
        ),
    ]
