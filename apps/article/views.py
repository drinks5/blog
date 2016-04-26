#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @belongto: root
# @Date:   2015-12-24 06:30:51
# @Last Modified by:   drinksober
# @Last Modified time: 2016-04-26 22:03:25

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.syndication.views import Feed
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, render_to_response
from django.core.urlresolvers import reverse_lazy, reverse
from django.db.models import Count
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  UpdateView, View, ListView, YearArchiveView,
                                  MonthArchiveView, FormView, TemplateView)
from braces.views import AjaxResponseMixin, JSONResponseMixin, LoginRequiredMixin
from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from textrank4zh import TextRank4Keyword, TextRank4Sentence

from .serializers import ArticleSerializer
from .models import Article, Comment, Category, Tag
from .forms import ContactForm, CommentForm


class HomeView(TemplateView):
    template_name = 'index.html'


class ContactView(TemplateView):
    template_name = 'contact.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ArticleView(TemplateView):
    template_name = 'article/post.html'


detail = ArticleView.as_view()


class ArticleEditView(TemplateView):
    template_name = 'article/edit.html'


class ArchiveView(TemplateView):
    template_name = 'article/archive.html'


class ArticleViewSet(viewsets.ViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    def get_queryset(self):
        queryset = Article.objects.filter(belongto=self.request.user)
        return queryset

    @detail_route(methods=['get'])
    def retrieve(self, request, pk):
        if pk:
            queryset = Article.objects.get(pk=pk)
            article_serializer = ArticleSerializer(queryset)
            return Response(article_serializer.data)
        return self.list(request)

    def list(self, request):
        article_serializer = ArticleSerializer(self.get_queryset(), many=True)
        return Response(article_serializer.data)

    @detail_route(methods=['post'])
    def create_or_update(self, request, pk=None):
        user = request.user
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        tr4w = TextRank4Keyword()
        tr4w.analyze(text=content, lower=True, window=2)
        tags = []
        for item in tr4w.get_keywords(3, word_min_len=1):
            tag = Tag.objects.get_or_create(belongto=user, name=item.word)[0]
            tags.append(tag)
        category = Category.objects.get_or_create(belongto=user,
                                                  name=tags[0])[0]
        tr4s = TextRank4Sentence()
        tr4s.analyze(text=content, lower=True, source='all_filters')
        summary = []
        for item in tr4s.get_key_sentences(num=3):
            summary.append(item.sentence)
        summary = ','.join(summary)
        if pk:
            article = Article.objects.get(pk=pk)
            article.tags.clear()
        else:
            article = Article()
        article.belongto = user
        article.title = title
        article.summary = summary
        article.content = content
        article.category = category
        article.save()
        article.tags.add(*tags)
        return Response(ArticleSerializer(article).data)


class ArticleDetail(JSONResponseMixin, AjaxResponseMixin, DetailView):
    model = Article

    def get_ajax(self, request, *args, **kwargs):
        return self.render_json_object_response([self.get_object()])


class ArticleMixin(object):
    model = Article
    template_name = 'article/edit_article.html'
    fields = ['title', 'content', 'category']

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.id})


class ArticleCreateView(ArticleMixin, CreateView):
    def form_valid(self, form, *args, **kwargs):
        form.instance.belongto = self.request.user
        return super(ArticleCreateView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        return HttpResponse('failure')


class ArticleUpdateView(ArticleMixin, UpdateView):
    def form_valid(self, form, *args, **kwargs):
        form.instance.belongto = self.request.user
        return super(ArticleUpdateView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self):
        return HttpResponse('failure')


class ArticleDeleteView(ArticleMixin, DeleteView):
    success_url = '/'

    def form_valid(self, form, *args, **kwargs):
        form.instance.belongto = self.request.user
        return super(ArticleDeleteView, self).form_valid(form, *args, **kwargs)


class ArchiveMixin(object):
    model = Article
    template_name = 'article/archive.html'
    context_object_name = 'post_list'


class Archive(ArchiveMixin, JSONResponseMixin, AjaxResponseMixin, ListView):
    def get_ajax(self, request, *args, **kwargs):
        return self.render_json_object_response(self.get_queryset())


class TagsArchive(ArchiveMixin, JSONResponseMixin, AjaxResponseMixin,
                  ListView):
    def get_ajax(self, request, *args, **kwargs):
        return self.render_json_object_response(self.get_queryset())

    def get_queryset(self):
        item = self.kwargs.get('item')
        queryset = Article.objects.annotate(Count('title')).filter(
            tags__name=item).prefetch_related('category').prefetch_related(
                'tags').order_by('timestamp')
        return queryset


class CategoryArchive(ArchiveMixin, ListView):
    def get_queryset(self):
        item = self.kwargs.get('item')
        queryset = Article.objects.annotate(Count('title')).filter\
            (category__name=item).prefetch_related('category')\
            .prefetch_related('tags').order_by('timestamp')
        return queryset


class TimeArchiveMixin(ArchiveMixin):
    """ abstract the TimeArchive's common feature """
    date_field = "timestamp"
    allow_future = True
    make_object_list = True


class YearArchive(TimeArchiveMixin, YearArchiveView):
    """year archive view"""
    pass


class MonthArchive(TimeArchiveMixin, MonthArchiveView):
    """month archive view"""
    pass


class BlogSearch(ArchiveMixin, ListView):
    """this function will search a post by title and content"""

    def get_queryset(self):
        errors = []
        keyword = self.request.GET.get('q', None)
        queryset = {}
        post_list = Article.objects.none()
        if not keyword:
            errors.append('please enter a search word...')
        elif len(keyword) > 20:
            errors.append('please enter at most 20 characters...')
        else:
            queryset['title'] = Article.objects.filter(
                title__icontains=keyword)
            queryset['content'] = Article.objects.filter(
                content__icontains=keyword)
        if not queryset:
            errors.append('no post was found...')
        elif queryset.get('title'):
            post_list = queryset.get('title')
        else:
            post_list = queryset.get('content')
        return post_list


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_msg = '/'

    def form_valid(self, form):
        return super(ContactView, self).form_valid(form)


contact = ContactView.as_view()


class RSSFeed(Feed):
    """this function offered the RSS page"""
    title = "RSS feed - Article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-timestamp')

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content


def display_meta(request):
    """just display all the request.META"""
    values = request.META.items()
    values.category()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table> ' % '\n'.join(html))


rss = RSSFeed()


class CommentActionMixin(object):
    model = Comment
    fields = ['text']
    template_name = "article/comment.html"

    def get_context_data(self, **kwargs):
        context = super(CommentActionMixin, self).get_context_data(self,
                                                                   **kwargs)
        post_id = self.kwargs.get('pk')
        context['post_id'] = post_id
        context['post'] = Article.objects.get(id=post_id)
        return super(CommentActionMixin, self).get_context_data(**kwargs)

    def form_invalid(self, form):
        return HttpResponse('failure')

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.kwargs.get('pk')})


class CommentCreateView(CommentActionMixin, CreateView):
    def form_valid(self, form):
        form.instance.belongto = self.request.user
        post_id = self.kwargs.get('pk')
        post = Article.objects.get(id=post_id)
        form.instance.post = post
        return super(CommentCreateView, self).form_valid(form)


create_comment = CommentCreateView.as_view()


class CommentDeleteView(CommentActionMixin, DeleteView):
    pass


delete_comment = CommentDeleteView.as_view()


class CommentView(View):
    form_class = CommentForm
    initial = {'key': 'value'}
    template_name = 'comment.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = int(self.instance.pk)
            comment.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})
