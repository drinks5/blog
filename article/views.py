# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.template import loader,Context
from django.http import Http404,HttpResponse
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib import messages
from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from markdown import markdown

# Create your views here.
def home(request):
    post_list = Article.objects.all()
    paginator = Paginator(post_list,5)
    page = request.GET.get('page')
    tags = Article.tags.all()
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.paginator(paginator.num_pages)
    return render(request,'home.html',{'post_list':posts, 'tag_list':tags })

def detail(request,my_args):
    post = get_object_or_404(Article,id=int(my_args) )
    return render(request,'post.html',{'post':post})

def archive(request):
    post_list = get_list_or_404(Article)

    return render(request,'archive.html',{'post_list':post_list,'error':False})

def blog_search(request):
    errors = []
    test = ['test','test2']
    if 'q' in request.GET:
        q = request.GET[ 'q']
        if not q:
            errors.append('please enter a search word...')
        elif len(q) > 20:
            errors.append( 'please enter at most 20 characters...')
        else:
            post_list = Article.objects.filter(title__icontains = q)
            if len( post_list) == 0:
                errors.append( 'no post was found...')
            else:
                return render( request, 'archive.html', { 'post_list': post_list, 'query':q})       
    return render( request, 'archive.html', { 'errors': errors, 'test':test })

class RSSFeed(Feed) :
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
    values = request.META.items()
    values.sort()
    html = []
    for k,v in values:
        html.append( '<tr><td>%s</td><td>%s</td></tr>' % (k,v ) )
    return HttpResponse( '<table>%s</table> ' % '\n'.join(html))
