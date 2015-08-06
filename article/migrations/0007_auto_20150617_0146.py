# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='avatar',
        ),
        migrations.AddField(
            model_name='article',
            name='avatar',
            field=models.ImageField(default=datetime.datetime(2015, 6, 17, 1, 46, 39, 9063, tzinfo=utc), upload_to=b'avatars'),
            preserve_default=False,
        ),
    ]
