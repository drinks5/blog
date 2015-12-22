# coding=utf-8
from django.db import models
from django.core.urlresolvers import reverse_lazy
from django.utils.encoding import python_2_unicode_compatible

from taggit.models import Tag
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from taggit.managers import TaggableManager

from accounts.models import User


@python_2_unicode_compatible
class Sort(models.Model):
    name = models.CharField(max_length=50)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '<{0}>'.format(self.name)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'category'
        ordering = ['name']


@python_2_unicode_compatible
class Article(models.Model):
    author = models.ForeignKey(User, related_name='+')
    title = models.CharField(max_length=50)
    summary = models.TextField(blank=True, null=True, max_length=400)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)
    tags = TaggableManager()
    sort = models.ForeignKey(Sort)
    avatar_thumbnail = ProcessedImageField(upload_to='avatars',      # source = 'avatar',
                                           processors=[ResizeToFill(480, 320)],
                                           format='JPEG',
                                           options={'quality': 60})

    def get_absolute_url(self):
        return reverse_lazy('article.views.detail', args=[str(self.id)])

    def __str__(self):
        return '<{0}: {1}>'.format(self.author, self.title)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = 'article'
        verbose_name_plural = 'article'


@python_2_unicode_compatible
class Comment(models.Model):
    author = models.ForeignKey(User, related_name='+')
    text = models.TextField()
    pub_timestamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Article)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comment'

    def __str__(self):
        return '<{0}: {1}>'.format(self.author, self.post.title)
