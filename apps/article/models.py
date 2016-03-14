# -*- coding: utf-8 -*-
# @Author: drinks
# @Date:   2016-03-09 16:22:29
# @Last Modified by:   drinks
# @Last Modified time: 2016-03-09 17:50:23
from django.db import models
from django.core.urlresolvers import reverse_lazy
from django.utils.encoding import python_2_unicode_compatible

from taggit.models import Tag
from taggit.managers import TaggableManager

from apps.accounts.models import User


# @python_2_unicode_compatible
# class Tags(Tag):

#     def __str__(self):
#         return '<{0}>'.format(self.values())


@python_2_unicode_compatible
class Sort(models.Model):
    name = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '<{0}>'.format(self.name)

    class Meta:
        verbose_name = u'分类'
        verbose_name_plural = u'分类'
        ordering = ['-create_date']


@python_2_unicode_compatible
class Article(models.Model):
    author = models.ForeignKey(User, related_name='+')
    title = models.CharField(max_length=50)
    # summary = models.TextField(blank=True, null=True, max_length=400)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)
    tags = TaggableManager()
    sort = models.ForeignKey(Sort)

    def get_absolute_url(self):
        return reverse_lazy('article.views.detail', args=(str(self.id),))

    def __str__(self):
        return '<{0}: {1}>'.format(self.author, self.title)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = u'文章'
        verbose_name_plural = u'文章'


@python_2_unicode_compatible
class Comment(models.Model):
    author = models.ForeignKey(User, related_name='+')
    text = models.TextField()
    pub_timestamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Article)

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = u'评论'

    def __str__(self):
        return '<{0}: {1}>'.format(self.author, self.post.title)
