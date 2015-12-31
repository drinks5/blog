#! /usr/bin/env python
# encoding: utf-8
__author__ = 'drinksober'

# Create your views here.
from django.template import RequestContext
from django.template.response import TemplateResponse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.syndication.views import Feed
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect, render_to_response
from django.core.mail import send_mail
from django.db.models import Count
from django.contrib import messages
from django.utils import timezone
from django.views.generic import (CreateView, UpdateView, DeleteView, DetailView,
                                  View, ListView, YearArchiveView,
                                  MonthArchiveView, FormView)

from .models import Article, Comment
from .forms import ContactForm, CommentForm
from accounts.views import LoginRequiredMixin


class HomeListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'home.html'
    paginate_by = 5
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['user'] = self.request.user
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


class ArticleMixin(object):
    model = Article
    template_name = 'edit_article.html'
    fields = ['title', 'content', 'tags', 'sort', 'avatar_thumbnail']


class ArticleCreateView(ArticleMixin, CreateView):
    success_url = reverse_lazy('')

    def form_valid(self, form, *args, **kwargs):
        form.instance.author = self.request.user
        return super(ArticleCreateView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        return HttpResponse('failure')


class ArticleUpdateView(ArticleMixin, UpdateView):

    def form_valid(self, form, *args, **kwargs):
        form.instance.author = self.request.user
        return super(ArticleUpdateView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self):
        return HttpResponse('failure')

class ArticleDeleteView(ArticleMixin, DeleteView):
    success_url = '/'

    def form_valid(self, form, *args, **kwargs):
        form.instance.author = self.request.user
        return super(ArticleDeleteView, self).form_valid(form, *args, **kwargs)


class ArchiveMixin(object):
    model = Article
    template_name = 'archive.html'
    context_object_name = 'post_list'


class ArchiveList(ArchiveMixin, ListView):
    pass

archive = ArchiveList.as_view()


class TagsArchiveList(ArchiveMixin, ListView):

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
            post_list = post_list_title
        else:
            post_list = post_list_content
        return post_list

blog_search = BlogSearchView.as_view()


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_msg = '/'

    def form_valid(self, form):
        pass


def contact(request):
    """this function offered the contact and send emailto site-owner"""
    errors = []
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cleaned_form_data = form.cleaned_data
            send_mail(
                cleaned_form_data['subject'],
                cleaned_form_data['message'],
                cleaned_form_data.get('email', 'drinksober@sina.com'),
                ['398869368@qq.com', '1349154991@qq.com'],
                fail_silently=False
            )
        return redirect('/contact/')
    else:
        form = ContactForm(
            initial={'subject': 'I love your site'}
        )
    return render(request, 'contact_from.html',
                  {'form': form}, context_instance=RequestContext(request))


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


@login_required
def add_comment(request, pk):
    """add comment by user in a post"""
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post_id = int(pk)
            comment.author_id = get_user(request).id
            comment.save()
            messages.add_message(request, messages.INFO, "comment complete")
        return HttpResponseRedirect(reverse(ArticleDetailView.as_view(), kwargs={'pk': 1}))
    else:
        form = CommentForm(initial={'key': 'value'})
    return redirect('article.views.home', error=True)


class CommentActionMixin(object):
    model = Comment
    # fields = ('author', 'post', 'text')
    fields = ('text',)
    template_name = "comment.html"

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(CommentActionMixin, self).form_valid(form)


class CommentCreateView(CommentActionMixin, CreateView):
    pass

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
            comment.post_id = int(pk)
            comment.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})
