# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0022_article_avatar_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='avatar_thumbnail',
            field=imagekit.models.fields.ProcessedImageField(upload_to=b'/avatars/'),
        ),
    ]
