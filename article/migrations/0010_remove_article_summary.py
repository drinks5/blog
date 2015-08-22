# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_auto_20150820_0103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='summary',
        ),
    ]
