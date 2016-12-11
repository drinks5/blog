# -*- coding: utf-8 -*-
# @Author: drinks
# @Date:   2016-03-15 16:07:50
# @Last Modified by:   drinksober
# @Last Modified time: 2016-04-26 22:27:14

from rest_framework import serializers
from blog.article.models import User
from .models import Article, Category
from taggit.models import Tag


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', )


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    belongto = UserSerializer(required=False)

    class Meta:
        model = Category
        fields = ('belongto', 'name', 'id')


class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'id')


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    belongto = UserSerializer()
    category = CategorySerializer()
    tags = CategorySerializer(many=True, read_only=True)
    background_thumbnail = serializers.ImageField(read_only=True)

    class Meta:
        model = Article
        fields = ('belongto', 'title', 'content', 'category', 'tags',
                  'update_date', 'id', 'background_thumbnail')
