from django.conf.urls import patterns, include, url
from django.contrib import admin
from article.views import RSSFeed

urlpatterns = patterns('',
    # Examples:
#    url(r'^$', 'mywebsite.views.home', name='home'),
#    url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
   # url(r'^$', 'article.views.home'),
    url(r'^$', 'article.views.home',name='home'),
    url(r'^(?P<my_args>\d+)/$', 'article.views.detail', name='detail'),
    url(r'^archive/', 'article.views.archive', name = 'archive'),
    url(r'^search/$','article.views.blog_search', name = 'search'),
    url(r'^feed/$', RSSFeed(),name = 'RSS'),

#    url(r'^test/$','blog.views.test'),
#   url(r'^tag(?P<tag>\w+)/$', 'blog.views.search_tag', name = 'search_tag'),
#   url(r'^display_meta/', 'blog.views.display_meta', name = 'display_meta'),
)
