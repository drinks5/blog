# coding=utf-8
from django.conf.urls import patterns, url,include 
from .views import *


archive_patterns = [
    url(r'^$', archive, name = 'archive'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',
        ArticleMonthArchiveView.as_view(month_format='%m'),
        name="archive_month"),
    url(r'^(?P<year>[0-9]{4})/$', ArticleYearArchiveView.as_view(), name='arcjove_year'),
    url(r'^category/(?P<item>\w+)/$', category_archive, name='archive_category'),
    url(r'^tags/(?P<item>\w+)/$', tags_archive, name='archive_tags'),
    ]

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', detail, name="detail"),
    url(r'^comment/(?P<pk>\d+)/$', add_Comment, name = 'comment'),

    url(r'^search/$',blog_search, name = 'search'),
    url(r'^meta/$', display_meta, name = 'meta'),
    url(r'^contact/$', contact, name = 'contact'),
    url(r'^aboutme/$', aboutme, name = 'aboutme'),
    url(r'^feed/$', RSSFeed(),name = 'RSS'),
    url(r'^archive/', include(archive_patterns)),

    ]
