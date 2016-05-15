from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from wkhtmltopdf.views import PDFTemplateView
from apps.article.views import (HomeView, ContactView, AboutView,
                                ArticleViewSet)
from rest_framework import routers
"((?P<pk>\d+)/)?$',"
router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet, base_name='article')
# api_patterns = [url(r'article/(?P<pk>\d+)?',
# ArticleViewSet.as_view({'post': 'create_or_update',
# 'get': 'retrieve'}))]
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^api-auth/',
        include('rest_framework.urls',
                namespace='rest_framework')),
    # url(r'^api/', include(api_patterns)),
    url(r'^api/', include(router.urls)),
    url(r'^article/', include('apps.article.urls')),
    url(r'^wechat/', include('apps.wechat.urls')),
    url(r'^(?P<page>\d*)$',
        HomeView.as_view(),
        name='home'),
    url(r'^contact/$',
        ContactView.as_view(),
        name='contact'),
    url(r'^about/$',
        AboutView.as_view(),
        name='about'),
    url(r'^pdf/$',
        PDFTemplateView.as_view(template_name='test.html',
                                filename='my_pdf.pdf'),
        name='pdf'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':
                                         settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root':
                                          settings.STATIC_ROOT}),
]
