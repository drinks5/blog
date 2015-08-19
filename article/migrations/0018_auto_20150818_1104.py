# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0017_auto_20150818_1102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='avatar',
            field=models.ImageField(upload_to=b'./media/avatars/'),
        ),
    ]
