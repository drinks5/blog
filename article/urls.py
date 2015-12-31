#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: drinks
# @Date:   2015-12-22 16:25:11
# @Last Modified by:   root
# @Last Modified time: 2015-12-26 19:30:35
# coding=utf-8

from django.conf.urls import patterns, url, include

from article.views import CommentCreateView, CommentDeleteView, RSSFeed, ArticleDetailView, ArchiveList


archive_patterns = patterns('article.views',
                            # url(r'^$', ArchiveList.as_view(), name = 'archive'),
                            url(r'^$', 'archive', name='archive'),
                            url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',
                                'month_archive', name="archive_month"),
                            url(r'^(?P<year>[0-9]{4})/$',
                                'year_archive', name='arcjove_year'),
                            url(r'^category/(?P<item>\w+)/$',
                                'category_archive', name='archive_category'),
                            url(r'^tags/(?P<item>\w+)/$',
                                'tags_archive', name='archive_tags'),
                            )

article_patterns = [
    url(r'^create/comment/$', CommentCreateView.as_view(),
        name='create comment'),
    # url(r'^update/com$', CommentUpdateView.as_view(),name = 'update comment'),
    url(r'^delete/comment/$', CommentDeleteView.as_view(),
        name='delete comment'),
]

urlpatterns = patterns('article.views',
                       url(r'^(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='detail'),
                       url(r'^comment/(?P<pk>\d+)/$',
                           CommentCreateView.as_view(), name='comment'),
                       url(r'^search/$', 'blog_search', name='search'),
                       url(r'^meta/$', 'display_meta', name='meta'),
                       url(r'^contact/$', 'contact', name='contact'),
                       url(r'^aboutme/$', 'aboutme', name='aboutme'),
                       url(r'^feed/$', RSSFeed(), name='RSS'),
                       url(r'^archive/', include(archive_patterns)),
                       )
