# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('article', '0027_article_tags1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tags1',
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
