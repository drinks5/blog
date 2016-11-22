from blog.article.models import Article
from . import factory


class TestArticle(BaseTestCase):
    def setUp(self):
        super(TestArticle, self).setUp()
        factory.ArticleFactory()
        self.user = factory.UserFactory()
        self.category = factory.CategoryFactory()
        self.url = '/api/article/'
        self.paras = {}

    def test_create_article(self):
        self.paras['title'] = 'title'
        self.paras['content'] = 'content'
        response = self.c.post(self.url, data=self.paras)
        # article = Article.objects.filter(title='title').get()
        # self.assertEqual(article.title, 'title')

    def test_update_article(self):
        article = Article.objects.create(
            belongto=self.user,
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
        response = self.c.get(self.url)
        print(response.content)
