from django.contrib import admin
from article.models import Article, Category
from django_admin_bootstrapped.admin.models import SortableInline


# Register your models here.

admin.site.register(Article)
admin.site.register(Category)

class Article(admin.StackedInline, SortableInline):
	model = Article
	extra = 0

