# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0030_article_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.CharField(max_length=300, null=True, blank=True),
        ),
    ]
