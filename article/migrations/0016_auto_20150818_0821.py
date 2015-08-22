# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_auto_20150818_0745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='avatar',
            field=models.ImageField(upload_to=b'/static/avatars'),
        ),
    ]
