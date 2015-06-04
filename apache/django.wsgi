import os
import sys

path = '/home/drinksober/Desktop/project/blog_site'
if path not in sys.path:
    sys.path.append(path)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'blog_site.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

