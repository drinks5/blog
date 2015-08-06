from django.db import models
from django.contrib import admin
from imagekit.models import ImageSpecField,ProcessedImageField
from imagekit.processors import ResizeToFill
from django.core.urlresolvers import reverse
from django_admin_bootstrapped.widgets import GenericContentTypeSelect


class Article(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=150,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True,null=True) 
    #  position = models.PositiveSmallIntegerField("Position")
    avatar = models.ImageField(upload_to = 'avatars')
    #avatar_thumbnail = ProcessedImageField(upload_to = 'avatars'        # source = 'avatar',
   #                                   processors = [ResizeToFill(100, 50)],
    #                                  format = 'JPEG',
     #                                 options = {'quality': 60})

    def get_absolute_url(self):
    	#path = reverse('detail', kwargs={'id':self.id})
        return ('detail', None, {'object.id':self.id})
     #   return "http://127.0.0.1:8000%s" 

    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['-timestamp']   

class Profile(models.Model):
    pass

class SomeModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ForeignKey:{'widget' : GenericContentTypeSelect},
    }



 #   link = models.URLField()    
 #   tags = models.CharField(max_length=10)

#class BlogPostAdmin(admin.ModelAdmin):
   # list_display = ('title','timestamp')
#admin.site.register(BlogPost)