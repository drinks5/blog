from django.conf.urls import patterns, url
from .views import profile

urlpatterns = patterns('accounts.views',
    url(r'^(?P<slug>\w+)',   profile, name = 'profile'),
    url(r'^login/$', 'login', name='login'),

    # url(r'^login/$', 'logout_then_login' , name='logout_then_login'),
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^password_change/$', 'password_change', name='password_change'),
    url(r'^password_change/done/$', 'password_change_done', name='password_change_done'),
    url(r'^password_reset/$', 'password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'password_reset_done', name='password_reset_done'),
    url(r'^reset/done/$', 'password_reset_complete', name='password_reset_complete'),
)

urlpatterns += patterns('accounts.views',
    url(r'^reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'password_reset_confirm_uidb36'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'password_reset_confirm',
        name='password_reset_confirm'),
    )
