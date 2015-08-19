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
    summary = models.TextField(max_length=300,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True,null=True) 
    tags = TaggableManager(blank=True)
    #tags = Tag.objects.all()

    #  position = models.PositiveSmallIntegerField("Position")
   # avatar = models.ImageField(upload_to = './media/avatars/')
    avatar_thumbnail = ProcessedImageField(  upload_to = './avatars/',         #source = 'avatar', ImageSpecField
                                        processors = [ ResizeToFill (480, 360)],
                                        format = 'JPEG',
                                        options = {'quality': 90})

    def get_absolute_url(self):
    	#path = reverse('detail', kwargs={'id':self.id})
        return ('detail', None, {'object.id':self.id})
     #   return "http://127.0.0.1:8000%s" 

    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['-timestamp']   



class SomeModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ForeignKey:{'widget' : GenericContentTypeSelect},
    }



 #   link = models.URLField()    
 #   tags = models.CharField(max_length=10)

#class BlogPostAdmin(admin.ModelAdmin):
   # list_display = ('title','timestamp')
#admin.site.register(BlogPost)