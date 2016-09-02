from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views.static import serve

from apps.article.views import ArticleViewSet, CategoryViewSet, TagViewSet
from rest_framework import routers

"((?P<pk>\d+)/)?$',"
router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet, base_name='article')
router.register(r'category', CategoryViewSet, base_name='category')
router.register(r'tags', TagViewSet, base_name='tags')
# api_patterns = [url(r'article/(?P<pk>\d+)?',
# ArticleViewSet.as_view({'post': 'create_or_update',
# 'get': 'retrieve'}))]
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api-auth/',
        include(
            'rest_framework.urls', namespace='rest_framework')),
    # url(r'^api/', include(api_patterns)),
    url(r'^api/', include(router.urls)),
    url(r'^article/', include('apps.article.urls')),
    url(r'^wechat/', include('apps.wechat.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':
                                         settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root':
                                          settings.STATIC_ROOT}),
]
