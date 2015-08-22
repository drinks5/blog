# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0018_auto_20150818_1104'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.RemoveField(
            model_name='article',
            name='avatar',
        ),
    ]
