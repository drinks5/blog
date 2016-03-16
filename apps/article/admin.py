# -*- coding: utf-8 -*-
# @Author: drinks
# @Date:   2016-03-09 13:14:06
# @Last Modified by:   drinks
# @Last Modified time: 2016-03-15 17:09:06
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.utils.html import format_html

from django_admin_bootstrapped.admin.models import SortableInline

from .models import Article, Comment, Category, Tags


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'category', 'timestamp')

    """
    show the avatar_thumbnail's url
    and it can callable
    """
    # readonly_fields = ("avatar_thumbnail",)
    #
    # def avatar_thumbnail(self, instance):
    #     url = reverse("avatar_detail", kwargs={"id": instance.pk})
    #     response = format_html("""<a href="{0}">{1}</a>""",url,url)
    #     return response
    #
    # avatar_thumbnail.short_description = "post avatar url"
    # avatar_thumbnail.allow_tags = True

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tags)

class Article(admin.StackedInline, SortableInline):
	model = Article
	extra = 0

