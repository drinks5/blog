# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20150818_0601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='avatar_thumbnail',
        ),
        migrations.AddField(
            model_name='article',
            name='avatar',
            field=models.ImageField(default=datetime.datetime(2015, 8, 18, 6, 53, 4, 976989, tzinfo=utc), upload_to=b'avatars'),
            preserve_default=False,
        ),
    ]
