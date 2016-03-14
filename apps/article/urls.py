# -*- coding: utf-8 -*-
# @Author: drinks
# @Date:   2015-12-22 16:25:11
# @Last Modified by:   drinks
# @Last Modified time: 2016-03-10 12:05:08


from django.conf.urls import patterns, url, include

from .views import CommentCreateView, CommentDeleteView, RSSFeed, ArticleDetailView, ArchiveList, ArticleCreateView, ArticleUpdateView, ArticleDeleteView


archive_patterns = patterns('apps.article.views',
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

comment_patterns = [
    url(r'^create/comment/$', CommentCreateView.as_view(),
        name='create comment'),
    # url(r'^update/com$', CommentUpdateView.as_view(),name = 'update comment'),
    url(r'^delete/comment/$', CommentDeleteView.as_view(),
        name='delete comment'),
]
article_patterns = [
    url(r'^create/$', ArticleCreateView.as_view(), name='create_article'),
    url(r'^update/(?P<pk>\d+)/$', ArticleUpdateView.as_view(), name='update_article'),
    url(r'^delete/(?P<pk>\d+)/$', ArticleDetailView.as_view(), name='delete_article')]

urlpatterns = patterns('apps.article.views',
                       url(r'', include(article_patterns)),
                       url(r'^(?P<pk>\d+)/$',
                           ArticleDetailView.as_view(), name='detail'),
                       url(r'^comment/(?P<pk>\d+)/$',
                           CommentCreateView.as_view(), name='comment'),
                       url(r'^search/$', 'blog_search', name='search'),
                       url(r'^meta/$', 'display_meta', name='meta'),
                       url(r'^contact/$', 'contact', name='contact'),
                       url(r'^aboutme/$', 'aboutme', name='aboutme'),
                       url(r'^feed/$', RSSFeed(), name='RSS'),
                       url(r'^archive/', include(archive_patterns)),
                       )
