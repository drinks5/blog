from django.contrib import admin
from article.models import Article, Sort, Comment
from django_admin_bootstrapped.admin.models import SortableInline


# Register your models here.

admin.site.register(Article)
admin.site.register(Sort)
admin.site.register(Comment)

class Article(admin.StackedInline, SortableInline):
	model = Article
	extra = 0

