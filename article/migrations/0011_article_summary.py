# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_remove_article_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.TextField(max_length=400, null=True, blank=True),
        ),
    ]
