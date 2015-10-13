from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/',include('django.contrib.admindocs.urls')),
    url(r'^accounts/', include('accounts.urls')),

    url(r'^article/',include('article.urls')),
    url(r'^(?P<page>\d*)$', 'article.views.home', name='home'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT }),
    url(r'^static/(?P<path>.*)$',serve,{'document_root':settings.STATIC_ROOT}),
    ]
