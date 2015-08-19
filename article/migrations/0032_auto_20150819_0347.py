# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0031_auto_20150819_0346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.TextField(null=True, blank=True),
        ),
    ]
