from blog.article.models import User
from blog.article.views import operate
def main():
    u = User.objects.first()
    for i in range(50):
        operate(u, 'title_{}'.format(i), 'content_{}'.format(i))
