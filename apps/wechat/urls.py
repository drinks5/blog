# -*- coding: utf-8 -*-
# @Author: drinks
# @Date:   2016-03-21 21:12:03
# @Last Modified by:   drinks
# @Last Modified time: 2016-03-21 21:42:27

from django.conf.urls import url

from .views import tokenView

urlpatterns = [url(r'', tokenView, name='tokenView'), ]
