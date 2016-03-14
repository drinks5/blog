from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

from apps.article.views import home

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/',include('django.contrib.admindocs.urls')),

    url(r'^accounts/', include('apps.accounts.urls')),
    url(r'^article/',include('apps.article.urls')),
    # url(r'^wx/',include('apps.wx.urls')),

    url(r'^(?P<page>\d*)$', home, name='home'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT }),
    url(r'^static/(?P<path>.*)$',serve,{'document_root':settings.STATIC_ROOT}),
    ]
