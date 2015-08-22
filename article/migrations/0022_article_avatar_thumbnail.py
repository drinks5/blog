# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import imagekit.models.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0021_remove_article_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='avatar_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(default=datetime.datetime(2015, 8, 18, 15, 56, 38, 684453, tzinfo=utc), upload_to=b'./media/avatars/'),
            preserve_default=False,
        ),
    ]
