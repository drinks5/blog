# -*- coding: utf-8 -*-
# @Author: drinks
# @Date:   2016-03-15 16:07:50
# @Last Modified by:   drinks
# @Last Modified time: 2016-03-16 10:55:52

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Article, Category, Tags

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username' ,'email')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    # belongto = UserSerializer(required=False)
    class Meta:
        model = Category
        fields = ('name',)

class TagsSerializer(serializers.HyperlinkedModelSerializer):
    # belongto = UserSerializer(required=False)
    class Meta:
        model = Tags
        fields = ('name',)

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer()
    category = CategorySerializer()
    class Meta:
        model = Article
        fields = ('author', 'title', 'content', 'category')
