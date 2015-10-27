# coding=utf-8
from django.conf.urls import patterns, url,include 

archive_patterns = patterns('article.views',
    # url(r'^$', ArchiveList.as_view(), name = 'archive'),
    url(r'^$', 'archive', name = 'archive'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$', 'month_archive',name="archive_month"),
    url(r'^(?P<year>[0-9]{4})/$', 'year_archive', name='arcjove_year'),
    url(r'^category/(?P<item>\w+)/$', 'category_archive', name='archive_category'),
    url(r'^tags/(?P<item>\w+)/$', 'tags_archive', name='archive_tags'),
    )

# article_patterns = [
#     url(r'^create/$', ArticleCreateView.as_view(),'name = create'),
#     url(r'^update/$', ArticleUpdateView.as_view(),'name = update'),
#     url(r'^delete/$', ArticleDeleteView.as_view(),'name = delete'),
#     ]

urlpatterns = patterns('article.views',
    url(r'^(?P<pk>\d+)/$', 'detail', name = 'detail'),
    url(r'^comment/(?P<pk>\d+)/$', 'add_comment', name = 'comment'),
    url(r'^search/$','blog_search', name = 'search'),
    url(r'^meta/$', 'display_meta', name = 'meta'),
    url(r'^contact/$', 'contact', name = 'contact'),
    url(r'^aboutme/$', 'aboutme', name = 'aboutme'),
    url(r'^feed/$', 'rss', name = 'RSS'),
    url(r'^archive/', include(archive_patterns)),
    )

