# -*- coding: utf-8 -*-
# @Author: linlin
# @Date:   2016-03-09 17:44:26
# @Last Modified by:   drinks
# @Last Modified time: 2016-03-09 18:24:39

from django.conf.urls import include, url
from .views import AuthView, GetUserInfoView, TestView,  WxSignature

urlpatterns = [
    # 授权
    url(r'^auth/$', AuthView.as_view(), name='wx_auth'),

    # 获取用户信息
    url(r'^code/$', GetUserInfoView.as_view(), name='get_user_info'),

    # 微信接口配置信息验证
    url(r'^$', WxSignature.as_view(), name='signature'),

    # 测试
    url(r'^test/$', TestView.as_view(), name='test_view'),

]
