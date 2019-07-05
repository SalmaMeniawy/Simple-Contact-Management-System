# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-07-04 08:15
from __future__ import unicode_literals

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20190704_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=phone_field.models.PhoneField(help_text='Contact mobile number', max_length=31),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=phone_field.models.PhoneField(help_text='Contact phone number', max_length=31),
        ),
    ]
