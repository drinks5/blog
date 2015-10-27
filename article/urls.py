# coding=utf-8
from django.conf.urls import patterns, url,include 
from .views import  (archive, ArchiveList , ArticleYearArchiveView, ArticleMonthArchiveView,
                                        category_archive, tags_archive, detail,add_comment, RSSFeed,
                                        blog_search, display_meta, contact, aboutme, ArticleDetailView)

archive_patterns = [ 
    # url(r'^$', ArchiveList.as_view(), name = 'archive'),
    url(r'^$', 'article.views.archive', name = 'archive'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]+)/$',
        ArticleMonthArchiveView.as_view(month_format='%m'),
        name="archive_month"),
    url(r'^(?P<year>[0-9]{4})/$', ArticleYearArchiveView.as_view(), name='arcjove_year'),
    url(r'^category/(?P<item>\w+)/$', category_archive, name='archive_category'),
    url(r'^tags/(?P<item>\w+)/$', tags_archive, name='archive_tags'),
    ]

# article_patterns = [
#     url(r'^create/$', ArticleCreateView.as_view(),'name = create'),
#     url(r'^update/$', ArticleUpdateView.as_view(),'name = update'),
#     url(r'^delete/$', ArticleDeleteView.as_view(),'name = delete'),
#     ]

urlpatterns = [
    # url(r'^(?P<pk>\d+)/$', ArticleDetailView.as_view(), name="detail"),
    url(r'^(?P<pk>\d+)/$', 'article.views.detail', name = 'detail'),

    url(r'^comment/(?P<pk>\d+)/$', add_comment, name = 'comment'),

    url(r'^search/$',blog_search, name = 'search'),
    url(r'^meta/$', display_meta, name = 'meta'),
    url(r'^contact/$', contact, name = 'contact'),
    url(r'^aboutme/$', aboutme, name = 'aboutme'),
    url(r'^feed/$', RSSFeed(),name = 'RSS'),
    url(r'^archive/', include(archive_patterns)),


    ]
