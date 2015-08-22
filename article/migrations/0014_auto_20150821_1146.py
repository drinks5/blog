# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_myprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.DeleteModel(
            name='MyProfile',
        ),
    ]
