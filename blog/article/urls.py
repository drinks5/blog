#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: drinks
# @Date:   2015-12-22 16:25:11
# @Last Modified by:   drinksober
# @Last Modified time: 2016-04-26 14:57:27

from rest_framework import routers
from django.conf.urls import url
from .views import ArticleViewSet, TagViewSet, CategoryViewSet, TokenViewSet
router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet, base_name='article')
router.register(r'tags', TagViewSet, base_name='tags')
router.register(r'category', CategoryViewSet, base_name='category')
router.register(r'token', TokenViewSet, base_name='token')

urlpatterns = router.urls
