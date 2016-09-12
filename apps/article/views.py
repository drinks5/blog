#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @belongto: root
# @Date:   2015-12-24 06:30:51
# @Last Modified by:   drinksober
# @Last Modified time: 2016-04-28 11:52:15

from django.db.models import Q
# Create your views here.
from django.shortcuts import get_object_or_404

from braces.views import (AjaxResponseMixin, JSONResponseMixin,
                          LoginRequiredMixin)
from rest_framework import viewsets
from rest_framework.response import Response
from taggit.models import Tag
from textrank4zh import TextRank4Keyword, TextRank4Sentence

from .forms import CommentForm
from .models import Article, Category, Comment
from .serializers import ArticleSerializer, CategorySerializer, TagSerializer


class CategoryViewSet(viewsets.ViewSet):
    def get_queryset(self):
        queryset = Category.objects.filter(status=1)
        return queryset

    def retrieve(self, request, pk):
        data = get_object_or_404(Category, pk=pk, status=1)
        data = CategorySerializer(data)
        return Response(data.data)

    def list(self, queryset):
        category_serializer = CategorySerializer(
            self.get_queryset(), many=True)
        return Response(category_serializer.data)


class TagViewSet(viewsets.ViewSet):
    def get_queryset(self):
        queryset = Tag.objects.filter()
        return queryset

    def retrieve(self, request, pk):
        data = get_object_or_404(Tag, pk=pk)
        data = TagSerializer(data)
        return Response(data.data)

    def list(self, queryset):
        data = TagSerializer(self.get_queryset(), many=True)
        return Response(data.data)


def get_search_q_obj(request):
    search = request.GET.get('search', '')
    if not search:
        return Q()
    query_para = Q(content__contains=search) | Q(title__contains=search) | Q(
        tags__name__contains=search) | Q(category__name__contains=search)
    return query_para


class ArticleViewSet(viewsets.ViewSet):
    def get_queryset(self):
        queryset = Article.objects.filter(status='1')
        return queryset

    def retrieve(self, request, pk):
        data = get_object_or_404(Article, pk=pk, status=1)
        article_serializer = ArticleSerializer(data)
        return Response(article_serializer.data)

    def list(self, request):
        query_para = get_search_q_obj(request)
        article_serializer = ArticleSerializer(
            self.get_queryset().filter(query_para).distinct(), many=True)
        return Response(article_serializer.data)

    def update(self, request, pk):
        return self._operate(request, pk)

    def create(self, request, pk=None):
        return self._operate(request, pk)

    def _operate(self, request, pk=None):
        user = request.user
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        tr4w = TextRank4Keyword()
        tr4w.analyze(text=content, lower=True, window=2)
        tags = []
        for item in tr4w.get_keywords(3, word_min_len=1):
            tag = Tag.objects.get_or_create(belongto=user, name=item.word)[0]
            tags.append(tag)
        category = Category.objects.get_or_create(
            belongto=user, name=tags[0])[0]
        tr4s = TextRank4Sentence()
        tr4s.analyze(text=content, lower=True, source='all_filters')
        summary = []
        for item in tr4s.get_key_sentences(num=3):
            summary.append(item.sentence)
        summary = ','.join(summary)
        paras = {'title': title,
                 'summary': summary,
                 'content': content,
                 'category': category,
                 'belongto': user}
        if pk:
            old_article = get_object_or_404(Article, pk=pk)
            old_article.tags.clear()
            paras.update({'pk': pk})
        article = Article(**paras)
        article.save()
        article.tags.add(*tags)
        return Response(ArticleSerializer(article).data)
