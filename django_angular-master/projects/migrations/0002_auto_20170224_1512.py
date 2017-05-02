# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userquestionanswer',
            name='answer_option',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='userquestionanswer',
            name='comment',
            field=models.CharField(default='comment', max_length=250),
            preserve_default=False,
        ),
    ]
