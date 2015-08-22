# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_article_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='avatar',
        ),
        migrations.AddField(
            model_name='article',
            name='avatar_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(default=2, upload_to=b'avatars'),
            preserve_default=False,
        ),
    ]
