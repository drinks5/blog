#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: drinks
# @Date:   2015-12-22 16:25:11
# @Last Modified by:   drinksober
# @Last Modified time: 2016-04-26 14:57:27

from django.conf.urls import url, include

from .views import (ArticleView, ArticleDetail, RSSFeed,
                    ArchiveView, Archive, TagsArchive, CategoryArchive,
                    YearArchive, MonthArchive, BlogSearch, display_meta,
                    ArticleEditView)

archive_patterns = [
    # url(r'^$', ArchiveList.as_view(), name = 'archive'),
    url(r'^$',
        Archive.as_view(),
        name='archive'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',
        MonthArchive.as_view(),
        name="archive_month"),
    url(r'^(?P<year>[0-9]{4})/$',
        YearArchive.as_view(),
        name='arcjove_year'),
    url(r'^category/(?P<item>\w+)/$',
        CategoryArchive.as_view(),
        name='archive_category'),
    url(r'^tags/(?P<item>\w+)/$',
        TagsArchive.as_view(),
        name='archive_tags'),
]

# comment_patterns = [
#     url(r'^create/comment/$', CommentCreateView.as_view(),
#         name='create comment'),
#     # url(r'^update/com$', CommentUpdateView.as_view(),name = 'update comment'),
#     url(r'^delete/comment/$', CommentDeleteView.as_view(),
#         name='delete comment'),
# ]
# article_patterns = [
#     url(r'^create/$', ArticleCreateView.as_view(), name='create_article'),
#     url(r'^update/(?P<pk>\d+)/$', ArticleUpdateView.as_view(), name='update_article'),
#     url(r'^delete/(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='delete_article')]

urlpatterns = [
    # url(r'', include(article_patterns)),
    url(r'^(?P<pk>\d+)/$',
        ArticleView.as_view(),
        name='detail_view'),
    url(r'^api/(?P<pk>\d+)/$',
        ArticleDetail.as_view(),
        name='detail'),
    url(r'^edit/((?P<pk>\d+)/)?$',
        ArticleEditView.as_view(),
        name='edit'),
    url(r'^search/$',
        BlogSearch.as_view(),
        name='search'),
    url(r'^meta/$',
        display_meta,
        name='meta'),
    url(r'^feed/$',
        RSSFeed(),
        name='RSS'),
    url(r'^archive/', include(archive_patterns)),
]
