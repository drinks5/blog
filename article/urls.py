# coding=utf-8
from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('article.views',
    url(r'^\d*^$', 'home',name='home'),
    url(r'^archive/', 'archive', name = 'archive'),
    url(r'^search/$','blog_search', name = 'search'),
    url(r'^meta/$', 'display_meta', name = 'meta'),
    url(r'^contact/$', 'contact', name = 'contact'),
    url(r'^article/(?P<pk>\d+)/$', 'detail', name='detail'),
    url(r'^category/(?P<item>\w+)/$', 'category_archive', name='category'),
    url(r'^comment/(?P<id>\d+)/$', 'add_Comment', name = 'comment'),
    url(r'^feed/$', RSSFeed(),name = 'RSS'),
    )