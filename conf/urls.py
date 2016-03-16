from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve

from apps.article.views import (HomeView, ContactView,
    AboutView)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/',include('django.contrib.admindocs.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # url(r'^accounts/', include('apps.accounts.urls')),
    url(r'^article/',include('apps.article.urls')),
    # url(r'^wx/',include('apps.wx.urls')),

    url(r'^(?P<page>\d*)$', HomeView.as_view(), name='home'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
    url(r'^about$', AboutView.as_view(), name='about'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT }),
    url(r'^static/(?P<path>.*)$',serve,{'document_root':settings.STATIC_ROOT}),
    ]
