# -*- coding: utf-8 -*-
# @Author: drinksober
# @Date:   2016-04-26 11:18:51
# @Last Modified by:   drinksober
# @Last Modified time: 2016-04-26 21:37:52

from django.contrib.auth.models import User
from django.test.client import Client

from apps.article.models import Article, Category, Tag
from .utils import BaseTestCase


class TestArticle(BaseTestCase):
    def setUp(self):
        super(TestArticle, self).setUp()
        self.user = User.objects.create_superuser(username='test',
                                                  password='123456',
                                                  email='test@test.com')
        self.paras = {}
        self.c = Client()
        self.c.login(username='test', password='123456')
        self.category = Category.objects.create(belongto=self.user,
                                                name='category')
        self.tag = Tag.objects.create(belongto=self.user, name='tag')

    def test_create_article(self):
        url = '/api/article/'
        self.paras['title'] = 'title'
        self.paras['content'] = 'content'
        response = self.c.post(url, data=self.paras)
        article = Article.objects.last()
        self.assertEqual(article.title, 'title')

    def test_update_article(self):
        article = Article.objects.create(belongto=self.user,
                                         title='title',
                                         content='content',
                                         category=self.category)
        url = '/api/article/' + str(article.id) + '/'
        self.paras['title'] = 'title1'
        self.paras['content'] = 'content1'
        response = self.c.post(url, data=self.paras)
        print(response.content)
        article = Article.objects.last()

    def test_get_list(self):
        url = '/api/article/'
        response = self.c.get(url)
        print(response.content)
