import factory
from blog.article.models import User
from blog.article.models import Article, Category


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'test{}'.format(n))
    email = factory.Sequence(lambda n: 'test{}@hypers.com'.format(n))
    is_superuser = True
    password = '123456'

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default ``_create`` with our custom call."""
        manager = cls._get_manager(model_class)
        # The default would use ``manager.create(*args, **kwargs)``
        return manager.create_user(*args, **kwargs)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    belongto = factory.SubFactory(UserFactory)
    name = factory.Sequence(lambda n: 'article category{}'.format(n))
    status = 1


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    belongto = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
    title = factory.Sequence(lambda n: 'article title{}'.format(n))
    summary = factory.Sequence(lambda n: 'article summary{}'.format(n))
    content = factory.Sequence(lambda n: 'article content{}'.format(n))
    status = 1
