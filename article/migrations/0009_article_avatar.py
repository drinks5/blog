# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_remove_article_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='avatar',
            field=models.ImageField(default=datetime.datetime(2015, 8, 18, 2, 59, 51, 347417, tzinfo=utc), upload_to=b'avatars'),
            preserve_default=False,
        ),
    ]
