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
from markdown import markdown

# Create your views here.
def home(request):
    post_list = Article.objects.all()
    paginator = Paginator(post_list,5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.paginator(paginator.num_pages)
    return render(request,'home.html',{'post_list':posts})

def detail(request,my_args):
    try:
        post = Article.objects.get(id=int(my_args))
     #   post.content = markdown(post.content)
     #   messages.success(request, "My success message")
     #   post = BlogPost.objects.all()[int(my_args)]
    except Article.DoesNotExist:
        raise Http404
   # str = ("title = %s, body =%s ,timestamp = %s" % (post.title,post.body,post.timestamp))
   # return HttpResponse(str)
    return render(request,'post.html',{'post':post})

def archive(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist :
        raise Http404
    return render(request,'archive.html',{'post_list':post_list,'error':False})

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'home.html')
        else:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render(request,'archive.html', {'post_list' : post_list,
                                                    'error' : True})
            else :
                return render(request,'archive.html', {'post_list' : post_list,
                                                    'error' : False})
    return redirect('/')

#this function hasn't finished
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

   # def item_link(self,item):
   #     return item.get_absolute_url()
      #  return reverse('news-item', args=[item.id])