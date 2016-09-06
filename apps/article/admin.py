# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Article, Comment, Category


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('belongto', 'title', 'category', 'update_date')
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


class Article(admin.StackedInline):
    model = Article
    extra = 0
