from django.db import models
from django.contrib import admin
from imagekit.models import ImageSpecField,ProcessedImageField
from imagekit.processors import ResizeToFill
from django.core.urlresolvers import reverse
from django_admin_bootstrapped.widgets import GenericContentTypeSelect
from taggit.managers import TaggableManager
from taggit.models import  Tag

class Article(models.Model):
    title = models.CharField(max_length=50)
    summary = models.TextField(blank=True,null=True,max_length=400) 
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True,null=True) 
    tags = TaggableManager()
    category = models.ForeignKey('Category')
    #  position = models.PositiveSmallIntegerField("Position")
   # avatar = models.ImageField(upload_to = 'avatars')
    avatar_thumbnail = ProcessedImageField(upload_to = 'avatars'  ,      # source = 'avatar',
                                      processors = [ResizeToFill(640  , 480)],
                                      format = 'JPEG',
                                      options = {'quality': 100})

    def get_absolute_url(self):
        #return reverse('article.view.detail', args=[str(self.id)])
        return '/%s/' % self.id

    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['-timestamp']   

class Category(models.Model):
      name = models.CharField(max_length=50)

      def __unicode__(self):
          return self.name

      class Meta:
          ordering = ['name']


