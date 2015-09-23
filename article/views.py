# Create your views here.
from article.models import Article
from django.template import RequestContext
from django.http import Http404,HttpResponse
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect,render_to_response
from django.core.mail import send_mail
from article.forms import ContactForm
from django.db.models import Count
"""
from django.contrib import messages
from django.core.urlresolvers import reverse
from datetime import datetime
"""
# Create your views here.
"""
the home page and it will display 5 posts per page
"""
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

"""
the function will display the detail of a post
"""
def detail(request,my_args):
    post = get_object_or_404(Article,id=int(my_args) )
    return render(request,'post.html',{'post':post})

"""
this function will make archive of all the post
"""

def archive(request):
    post_list = get_list_or_404(Article)
    return render(request,'archive.html',{'post_list':post_list,'error':False})


"""
archive by tags
"""
def tags_archive(request, item):
    post = Article.objects.annotate(Count('title')).filter\
        (tags__name= item).prefetch_related('category')\
        .prefetch_related('tags').order_by('timestamp')

def category_archive(request, item):
    post = Article.objects.annotate(Count('title')).filter\
        (category__name= item).prefetch_related('category')\
        .prefetch_related('tags').order_by('timestamp')
"""
this function will search a post by title and content
"""
def blog_search(request):
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

"""
this function offered the contact and send email
to site-owner
"""
def contact(request):
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
    return render(request, 'contact_from.html', {'form':form}, context_instance=RequestContext(request))



"""
this function offered the RSS page
"""
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
