# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ask_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tags',
            name='text',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]
