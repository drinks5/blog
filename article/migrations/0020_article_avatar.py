# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0019_auto_20150818_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='avatar',
            field=models.ImageField(default=1, upload_to=b'./media/avatars/'),
            preserve_default=False,
        ),
    ]
