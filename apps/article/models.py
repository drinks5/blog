# -*- coding: utf-8 -*-
# @Author: drinks
# @Date:   2016-03-09 16:22:29
# @Last Modified by:   drinksober
# @Last Modified time: 2016-04-26 21:59:26
from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# from apps.accounts.models import User

status_choices = ((0, 'deleted'), (1, 'active'))


class Category(models.Model):
    belongto = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=status_choices, default=1)

    def __str__(self):
        return '<{0}: {1}>'.format(self.belongto, self.name)

    class Meta:
        verbose_name = u'分类'
        verbose_name_plural = u'分类'
        ordering = ['-create_date']


class Article(models.Model):
    belongto = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    summary = models.TextField(blank=True, null=True, max_length=400)

    content = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category)
    tags = TaggableManager()
    status = models.IntegerField(choices=status_choices, default=1)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    background = models.ImageField(upload_to='background')
    background_thumbnail = ImageSpecField(
        source='background',
        processors=[ResizeToFill(900, 300)],
        format='JPEG',
        options={'quality': 60})

    def get_absolute_url(self):
        return '/article/{0}/'.format(self.pk)

    def __str__(self):
        return '<{0}: {1}>'.format(self.belongto, self.title)

    class Meta:
        ordering = ['-update_date']
        verbose_name = u'文章'
        verbose_name_plural = u'文章'


class Comment(models.Model):
    belongto = models.ForeignKey(User)
    text = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey(Article)
    status = models.IntegerField(choices=status_choices, default=1)

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = u'评论'

    def __str__(self):
        return '<{0}: {1}>'.format(self.belongto, self.post.article)
