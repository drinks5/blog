DEBUG = False
DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME'    : 'article',
        'USER'     : 'root',
        'PASSWORD'  : 'drinks',
        'HOST'   : '',
        'PORT'   : '3306',
    }
    }

    INSTALLED_APPS = (
    'django.contrib.admindocs',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # 'authtools',
    'bootstrap3',
    'imagekit',
    'taggit',
    'rest_framework',
#    'userena',
#    'guardian',
#    'easy_thumbnails',
 #   'django-debug-toolbar',
    'accounts',
    'article',
)