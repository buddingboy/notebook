# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-08 04:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0010_remove_note_prelims'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='prelims',
            field=models.BooleanField(default=False),
        ),
    ]
