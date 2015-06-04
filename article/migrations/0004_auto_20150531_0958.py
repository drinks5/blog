# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_auto_20150531_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='link',
        ),
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
    ]
