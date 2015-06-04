from django.db import models
from django.contrib import admin
from django.core.urlresolvers import reverse

class Article(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=150,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True,null=True) 

    def get_absolute_url(self):
    	#path = reverse('detail', kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" 

    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['-timestamp']   
 #   link = models.URLField()    
 #   tags = models.CharField(max_length=10)


#class BlogPostAdmin(admin.ModelAdmin):
   # list_display = ('title','timestamp')
#admin.site.register(BlogPost)