from django.test import TestCase

from accounts.models import User
from article.models import Article, Comment, Sort
#Create your tests here.


user = User.objects.all()[0]

class ArticleMethodTest(TestCase):
    def craete(self):
        Article.objecs.create(title='test',author=user, sort=Sort.objects.get(id=1))