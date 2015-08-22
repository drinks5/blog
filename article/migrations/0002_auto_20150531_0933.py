# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=20, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(null=True, blank=True)),
                ('link', models.URLField()),
                ('tags', models.CharField(max_length=5)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
    ]
