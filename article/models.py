# coding=utf-8
from django.db import models
from django.contrib import admin
from imagekit.models import ImageSpecField,ProcessedImageField
from imagekit.processors import ResizeToFill
from django.core.urlresolvers import reverse
from django_admin_bootstrapped.widgets import GenericContentTypeSelect
from taggit.managers import TaggableManager
from taggit.models import  Tag
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length=50)
    summary = models.TextField(blank=True,null=True,max_length=400) 
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True,null=True) 
    tags = TaggableManager()
    category = models.ForeignKey('Category')
 #   click_num = models.IntegerField( default=0 )
    avatar_thumbnail = ProcessedImageField(upload_to = 'avatars'  ,      # source = 'avatar',
                                      processors = [ResizeToFill(640  , 480)],
                                      format = 'JPEG',
                                      options = {'quality': 100})

    def get_absolute_url(self):
        #return reverse('article.view.detail', args=[str(self.id)])
        return '/%s/' % self.id

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name = u'文章'
        verbose_name_plural = u'文章'

@python_2_unicode_compatible
class Category(models.Model):
      name = models.CharField(max_length=50)

      def __str__(self):
          return self.name

      class Meta:
          verbose_name = u'目录分类'
          verbose_name_plural = u'目录分类'
          ordering = ['name']

@python_2_unicode_compatible
class comment(models.Model):
    author = models.CharField(max_length=20)
    email = models.EmailField()
    text = models.TextField()
    pub_timestamp = models.DateTimeField(auto_now_add=True)
 #   post = models.ForeignKey(Post)

    class Meta:
        verbose_name = u'评论'
        verbose_name_plural = u'评论'

    def __str__(self):
        return self.author
      #  return '{0}: {1}'.format(self.author, self.post.title)