# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-04-28 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default='Images/None/NoImg.jpg', upload_to='Images/'),
        ),
    ]