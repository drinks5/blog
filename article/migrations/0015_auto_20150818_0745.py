# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0014_auto_20150818_0734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='avatar_thumbnail',
        ),
        migrations.AddField(
            model_name='article',
            name='avatar',
            field=models.ImageField(default=1, upload_to=b'avatars'),
            preserve_default=False,
        ),
    ]
