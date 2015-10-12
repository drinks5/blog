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
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect,render_to_response
from django.core.mail import send_mail
from django.db.models import Count
from django.views.generic import CreateView, UpdateView, DetailView, View
from django.contrib import messages
from django.utils import timezone

from .models import Article, Comment
from .forms import ContactForm, CommentForm


# Create your views here.
@login_required
def home(request,page):
    """the home page and it will display 5 posts per page"""
    post_list = Article.objects.all()
    paginator = Paginator(post_list,5)
    page = request.GET.get('page')
    tags = Article.tags.all()
    sorts = Article.sort.get_queryset()
    user = get_user(request)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.paginator(paginator.num_pages)
    return render(request,'home.html',
                  {'post_list':posts, 'tag_list':tags,'sort_list': sorts , 'user': user })

def detail(request,pk):
    """the function will display the detail of a post"""
    post = get_object_or_404(Article, id=int(pk))
    comments = post.comment_set.all()
    return render(request,'post.html',{'post':post, 'comments': comments, 'error':False})

# class ArticleDetailView(DetailView):
#     model = Article
#     template_name = 'detail.html'

#     def get_context_data(self, **kwargs):
#         context = super(ArticleDetailView, self).get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context
# detail = ArticleDetailView.as_view()

def archive(request):
    """this function will make archive of all the post"""
    post_list = get_list_or_404(Article)
    return render(request,'archive.html',{'post_list':post_list,'error':False})

def aboutme(request):
    """the AboutMe page"""
    return  render(request, 'aboutme.html',{})


def tags_archive(request, item):
    """archive by tags"""
    posts = Article.objects.annotate(Count('title')).filter\
        (tags__name= item).prefetch_related('sort')\
        .prefetch_related('tags').order_by('timestamp')
    return render(request, 'archive.html', { 'post_list': posts })

def category_archive(request, item):
    posts = Article.objects.annotate(Count('title')).filter\
        (sort__name= item).prefetch_related('sort')\
        .prefetch_related('tags').order_by('timestamp')
    return render(request, 'archive.html', { 'post_list': posts })

def blog_search(request):
    """this function will search a post by title and content"""
    errors = []
    keyWord = Article.objects.none()
    if 'q' in request.GET:
        q = request.GET[ 'q']
        if not q:
            errors.append('please enter a search word...')
        elif len(q) > 20:
            errors.append( 'please enter at most 20 characters...')
        else:
            post_list_title =   Article.objects.filter(  title__icontains = q)
            post_list_content = Article.objects.filter(content__icontains = q)
            if len( post_list_title) == 0 :
                if len(post_list_content) == 0:
                    errors.append( 'no post was found...')
                else:
                    keyWord = post_list_content
            else:
                keyWord = post_list_title
            return render( request, 'archive.html', { 'post_list': keyWord, 'query':q})
    return render( request, 'archive.html', { 'errors': errors,})

def contact(request):
    """this function offered the contact and send emailto site-owner"""
    errors = []
    if request.method ==  'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cleaned_form_data = form.cleaned_data
            send_mail(
                cleaned_form_data['subject'],
                cleaned_form_data['message'],
                cleaned_form_data.get('email','drinksober@sina.com'),
                ['398869368@qq.com', '1349154991@qq.com'],
                fail_silently=False
                )
        return redirect('/contact/')
    else:
        form = ContactForm(
            initial = { 'subject':'I love your site'}
        )
    return render(request, 'contact_from.html',
                  {'form':form}, context_instance=RequestContext(request))


def add_Comment(request,pk):
    """add comment by user in a post"""
    if request.method == 'POST':
        form = CommentForm( request.POST)
        if form.is_valid():
            comment = form.save( commit = False)
            comment.post_id = int(pk)
            comment.save()
        return redirect( 'article.views.detail', pk = pk)
    else:
        form = CommentForm(initial={ 'key': 'value'})
    return redirect( 'article.views.home',error=True)


class RSSFeed(Feed) :
    """this function offered the RSS page"""
    title = "RSS feed - Article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-timestamp')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

def display_meta(request):
    """just display all the request.META"""
    values = request.META.items()
    values.sort()
    html = []
    for k,v in values:
        html.append( '<tr><td>%s</td><td>%s</td></tr>' % (k,v ) )
    return HttpResponse( '<table>%s</table> ' % '\n'.join(html))

class CommentActionMixin(object):
    fields = ('author', 'email', 'text')

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info( self.request, self.sucess_msg)
        return super(CommentActionMixin, self).form_valid(form)

class CommentCreateView(CommentActionMixin, CreateView):
    model = Comment
    success_msg ="Comment created!!!"

class CommentUpdateView(CommentActionMixin, UpdateView):
    model = Comment
    success_msg ="Comment updated!!!"

class CommentDetailView( DetailView):
    model = Comment
    template_name = 'comment.html'
    context_object_name = 'comment'

class CommentView( View):
    form_class = CommentForm
    initial = { 'key': 'value'}
    template_name = 'comment.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial= self.initial)
        return render( request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            comment = form.save( commit = False)
            comment.post_id = int(pk)
            comment.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name,{'form':form})
