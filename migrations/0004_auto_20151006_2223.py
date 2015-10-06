# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask_app', '0003_auto_20151006_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to=b'/Users/kobronah/PycharmProjects/ask_project/ask_app/static/ask_app', blank=True),
        ),
    ]
