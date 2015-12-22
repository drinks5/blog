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
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect, render_to_response
from django.core.mail import send_mail
from django.db.models import Count
from django.contrib import messages
from django.utils import timezone
from django.views.generic import (CreateView, DeleteView, DetailView,
                                  View, ListView, YearArchiveView,
                                  MonthArchiveView)

from .models import Article, Comment
from .forms import ContactForm, CommentForm


class HomeListView(ListView):
    model = Article
    template_name = 'home.html'
    paginate_by = 5
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        context['user'] = get_user(self.request)
        context['tags'] = Article.tags.all()
        context['sort_list'] = Article.sort.get_queryset()
        return context

home = HomeListView.as_view()

# def detail(request,pk):
#     """the function will display the detail of a post"""
#     post = get_object_or_404(Article, id=int(pk))
#     comments = post.comment_set.all()
# return render(request,'post.html',{'post':post, 'comments': comments,
# 'error':False})


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'post.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['user'] = get_user(self.request)
        context['comments'] = Comment.objects.filter(post__id=int(pk))
        return context


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


class TimeArchiveMixin(object):

    """ abstract the TimeArchive's common feature """
    queryset = Article.objects.all()
    date_field = "timestamp"
    allow_future = True


class ArticleYearArchiveView(TimeArchiveMixin, YearArchiveView):

    """year archive view"""
    make_object_list = True
    template_name = 'year_archive.html'

year_archive = ArticleYearArchiveView.as_view()


class ArticleMonthArchiveView(TimeArchiveMixin, MonthArchiveView):

    """month archive view"""
    template_name = 'month_archive.html'

month_archive = ArticleMonthArchiveView.as_view()


def aboutme(request):
    """the AboutMe page"""
    user = get_user(request)
    return render(request, 'aboutme.html', {'user': user})


def blog_search(request):
    """this function will search a post by title and content"""
    errors = []
    keyWord = Article.objects.none()
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('please enter a search word...')
        elif len(q) > 20:
            errors.append('please enter at most 20 characters...')
        else:
            post_list_title = Article.objects.filter(title__icontains=q)
            post_list_content = Article.objects.filter(content__icontains=q)
            if len(post_list_title) == 0:
                if len(post_list_content) == 0:
                    errors.append('no post was found...')
                else:
                    keyWord = post_list_content
            else:
                keyWord = post_list_title
            return render(request, 'archive.html', {'post_list': keyWord, 'query': q})
    return render(request, 'archive.html', {'errors': errors, })


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
        return HttpResponseRedirect(reverse(detail, kwargs={'pk': pk}))
    else:
        form = CommentForm(initial={'key': 'value'})
    return redirect('article.views.home', error=True)


class CommentActionMixin(object):
    model = Article
    fields = ('author', 'email', 'text')
    template_name = "comment.html"

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.sucess_msg)
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
