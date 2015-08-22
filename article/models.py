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
  #  tags = TaggableManager()
    #  position = models.PositiveSmallIntegerField("Position")
   # avatar = models.ImageField(upload_to = 'avatars')
    avatar_thumbnail = ProcessedImageField(upload_to = 'avatars'  ,      # source = 'avatar',
                                      processors = [ResizeToFill(640  , 480)],
                                      format = 'JPEG',
                                      options = {'quality': 100})

    def get_absolute_url(self):
    	#path = reverse('detail', kwargs={'id':self.id})
        return ('detail', None, {'object.id':self.id})
     #   return "http://127.0.0.1:8000%s" 

    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['-timestamp']   



