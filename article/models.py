from django.db import models
from django.contrib import admin
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.core.urlresolvers import reverse

class Article(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=150,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True,null=True) 

    def get_absolute_url(self):
    	#path = reverse('detail', kwargs={'id':self.id})
       
        return ('detail', None, {'object.id':self.id})
     #   return "http://127.0.0.1:8000%s" 

    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['-timestamp']   

class Profile(models.Model):
    avatar = models.ImageField(upload_to = 'avatars')

    avatar_thumbnail = ImageSpecField(source = 'avatar',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})
"""
profile = Profile.objects.all()[0]
print profile.avatar_thumbnail.url
print profile.avatar_thumbnail.width
"""
 #   link = models.URLField()    
 #   tags = models.CharField(max_length=10)


#class BlogPostAdmin(admin.ModelAdmin):
   # list_display = ('title','timestamp')
#admin.site.register(BlogPost)