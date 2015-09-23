from django.conf.urls import patterns, include, url
#from django.conf.urls.default import *
from django.contrib import admin
from article.views import RSSFeed
from django.conf import settings
#from article import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^feed/$', RSSFeed(),name = 'RSS'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
                       )

urlpatterns += patterns('article.views',
    url(r'^$', 'home',name='home'),
    url(r'^archive/', 'archive', name = 'archive'),
    url(r'^search/$','blog_search', name = 'search'),
    url(r'^meta/$', 'display_meta', name = 'meta'),
    url(r'^contact/$', 'contact', name = 'contact'),
    url(r'^(?P<my_args>\d+)/$', 'detail', name='detail'),
    url(r'^category/(?P<item>\w+)/$', 'category_archive', name='category'),
    )


"""
the archive about all post
"""
