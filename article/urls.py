# coding=utf-8
from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('article.views',
    
    url(r'archive/', archive, name = 'archive'),
    url(r'(?P<pk>\d+)/$', detail, name='detail'),
    url(r'category/(?P<item>\w+)/$', category_archive, name='category'),
    url(r'tags/(?P<item>\w+)/$', tags_archive, name='tags'),
    url(r'comment/(?P<pk>\d+)/$', add_Comment, name = 'comment'),

    url(r'^search/$',blog_search, name = 'search'),
    url(r'^meta/$', display_meta, name = 'meta'),
    url(r'^contact/$', contact, name = 'contact'),
    url(r'^aboutme/$', aboutme, name = 'aboutme'),
    url(r'^feed/$', RSSFeed(),name = 'RSS'),

    )