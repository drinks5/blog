#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: root
# @Date:   2015-12-24 06:30:51
# @Last Modified by:   root
# @Last Modified time: 2015-12-26 19:13:50


# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.syndication.views import Feed
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, render_to_response
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy, reverse
from django.db.models import Count
from django.contrib import messages
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  View, ListView, YearArchiveView,
                                  MonthArchiveView, FormView)

from braces.views import AjaxResponseMixin, JSONResponseMixin
from .models import Article, Comment
from .forms import ContactForm, CommentForm
from accounts.views import LoginRequiredMixin
from accounts.models import User


class HomeListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'home.html'
    paginate_by = 5
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['user'] = get_user(self.request)
        context['tag_list'] = Article.tags.all()
        context['sort_list'] = Article.sort.get_queryset()
        return context

home = HomeListView.as_view()


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk', None)
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['user'] = get_user(self.request)
        context['comments'] = Comment.objects.filter(post__id=int(pk))
        return context

detail = ArticleDetailView.as_view()


class ArchiveMixin(object):
    model = Article
    template_name = 'archive.html'
    context_object_name = 'post_list'


class ArchiveList(ArchiveMixin, JSONResponseMixin, AjaxResponseMixin, ListView):

    def get_ajax(self, request, *args, **kwargs):
        return self.render_json_object_response(self.get_queryset())

archive = ArchiveList.as_view()


class TagsArchiveList(ArchiveMixin, JSONResponseMixin, AjaxResponseMixin,  ListView):

    def get_ajax(self, request, *args, **kwargs):
        return self.render_json_object_response(self.get_queryset())

    def get_queryset(self):
        item = self.kwargs.get('item')
        queryset = Article.objects.annotate(Count('title')).filter\
            (tags__name=item).prefetch_related('sort')\
            .prefetch_related('tags').order_by('timestamp')
        return queryset

tags_archive = TagsArchiveList.as_view()


class CategoryList(ArchiveMixin, ListView):

    def get_queryset(self):
        item = self.kwargs.get('item')
        queryset = Article.objects.annotate(Count('title')).filter\
            (sort__name=item).prefetch_related('sort')\
            .prefetch_related('tags').order_by('timestamp')
        return queryset

category_archive = CategoryList.as_view()


class TimeArchiveMixin(ArchiveMixin):

    """ abstract the TimeArchive's common feature """
    date_field = "timestamp"
    allow_future = True
    make_object_list = True


class ArticleYearArchiveView(TimeArchiveMixin, YearArchiveView):

    """year archive view"""
    pass


year_archive = ArticleYearArchiveView.as_view()


class ArticleMonthArchiveView(TimeArchiveMixin, MonthArchiveView):

    """month archive view"""
    pass

month_archive = ArticleMonthArchiveView.as_view(month_format='%m')


def aboutme(request):
    """the AboutMe page"""
    user = get_user(request)
    return render(request, 'aboutme.html', {'user': user})


class BlogSearchView(ArchiveMixin, ListView):

    """this function will search a post by title and content"""

    def get_queryset(self):
        errors = []
        keyword = self.kwargs.get('q', None)
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

blog_search = BlogSearchView.as_view()


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
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table> ' % '\n'.join(html))

rss = RSSFeed()


class CommentActionMixin(object):
    model = Comment
    fields = ['text']
    template_name = "comment.html"

    def get_context_data(self, **kwargs):
        context['post_id'] = self.kwargs.get('pk')
        context['post'] = Article.objects.get(id=post_id)
        return super(CommentActionMixin, self).get_context_data(**kwargs)

    def form_invalid(self, form):
        return HttpResponse('failure')

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.kwargs.get('pk')})


class CommentCreateView(CommentActionMixin, LoginRequiredMixin, CreateView):

    def form_valid(self, form):
        form.instance.author = self.request.user
        post_id = self.kwargs.get('pk')
        post = Article.objects.get(id=post_id)
        form.instance.post = post
        # messages.info(self.request, self.success_msg)
        return super(CommentCreateView, self).form_valid(form)

create_comment = CommentCreateView.as_view()


class CommentDeleteView(CommentActionMixin, LoginRequiredMixin, DeleteView):
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
            comment.post_id = int(pk)
            comment.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})
