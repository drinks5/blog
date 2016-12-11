# -*- coding: utf-8 -*-
"""
Django settings for blog project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import environ

PROJECT_NAME = 'blog'
ROOT_DIR = environ.Path(
    __file__) - 3  # (blog/config/settings/common.py - 3 = blog/)
CONFIG_DIR = ROOT_DIR.path('config')
APPS_DIR = ROOT_DIR.path('blog')
STATIC_DIR = APPS_DIR.path('static')
FE_DIR = ROOT_DIR.path('front-end/dist')


env = environ.Env()
env.read_env()

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', )
THIRD_PARTY_APPS = ('rest_framework', 'imagekit', 'django_nose', 'taggit')

# Apps specific for this project go here.
LOCAL_APPS = (
    # Your stuff: custom apps go here
    'blog.article', )
# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.common.CommonMiddleware',  # 是否使用etags?
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'cas.middleware.CASMiddleware',
    'config.aspect.middleware.AspectMiddleware')

# SITE CONFIGURATION
# ------------------------------------------------------------------------------
# Hosts/domain names that are valid for this site
# See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list('DJANGO_ALLOWED_HOSTS') or '*'
# END SITE CONFIGURATION

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', False)

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.smtp.EmailBackend')

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'NAME': env('MYSQL_NAME') or 'blog',
#         'HOST': env('MYSQL_HOST') or '127.0.0.1',
#         'USER': env('MYSQL_USER') or 'root',
#         'PASSWORD': env('MYSQL_PASSWORD') or '123456',
#         'PORT': env('MYSQL_PORT') or '3306',
#         'ENGINE': 'django.db.backends.mysql',
#         'OPTIONS': {
#             'autocommit': True,
#         },
#     }
# }
# DATABASES['default']['ATOMIC_REQUESTS'] = False  # 每个view 是否用 事务

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(CONFIG_DIR.path('db.sqlite3')),
    }
}
# CACHES
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# SESSION
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_REDIS_HOST = env('REDIS_HOST') or 'localhost'
SESSION_REDIS_PORT = env('REDIS_PORT') or 6379
SESSION_REDIS_PASSWORD = env('REDIS_PASSWORD') or '123456'
SESSION_REDIS_DB = 0
SESSION_REDIS_PREFIX = 'session'
SESSION_REDIS_SOCKET_TIMEOUT = 1
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

USE_TZ = True

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-TEMPLATES-BACKEND
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-dirs
        'DIRS': [str(APPS_DIR.path('templates')), ],
        'OPTIONS': {
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
            'debug': DEBUG,
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-loaders
            # https://docs.djangoproject.com/en/dev/ref/templates/api/#loader-types
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            # See: https://docs.djangoproject.com/en/dev/ref/settings/#template-context-processors
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                # Your stuff: custom template context processors go here
            ],
        },
    },
]

# See: http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(FE_DIR.path('static'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (str(STATIC_DIR.path('static')), )

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder', )

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(STATIC_DIR('media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    # 'backends.cas_backends.CASBackend',
    # 'backends.email_backends.EmailBackend',
)

# Custom user app defaults
# Select the correct user model

# Your common stuff: Below this line define 3rd party library settings
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    # Use Django's standard 'django.contrib.auth' permissions ,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_AUTHENTICATION_CLASSES':
    ('rest_framework.authentication.TokenAuthentication', ),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny', ),
    'DEFAULT_PERMISSION_CLASSES':
    ['rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'],
    'PAGE_SIZE': 5,
    'DATETIME_FORMAT': "%Y-%m-%d",
}
AUTH_USER_MODEL = 'article.User'
