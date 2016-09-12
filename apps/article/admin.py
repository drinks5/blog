# -*- coding: utf-8 -*-
from django.contrib import admin
from django.db import models
from pagedown.widgets import AdminPagedownWidget

from .models import Article, Category, Comment


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('belongto', 'title', 'category', 'update_date')
    formfield_overrides = {models.TextField: {'widget': AdminPagedownWidget}, }


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Category)
