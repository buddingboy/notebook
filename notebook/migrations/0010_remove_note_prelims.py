# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-08-08 04:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0009_note_prelims'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='prelims',
        ),
    ]