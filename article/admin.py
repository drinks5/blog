from django.contrib import admin
from article.models import Article
from django_admin_bootstrapped.admin.models import SortableInline
from models import Article

# Register your models here.
admin.site.register(Article)
class Article(admin.StackedInline, SortableInline):
	model = Article
	extra = 0


