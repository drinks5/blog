# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import imagekit.models.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0009_article_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='avatar',
        ),
        migrations.AddField(
            model_name='article',
            name='avatar_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(default=datetime.datetime(2015, 8, 18, 6, 1, 25, 143796, tzinfo=utc), upload_to=b'avatars'),
            preserve_default=False,
        ),
    ]
