# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0008_remove_article_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='category',
            new_name='summary',
        ),
        migrations.AddField(
            model_name='article',
            name='avatar_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(default=1, upload_to=b'avatars'),
            preserve_default=False,
        ),
    ]
