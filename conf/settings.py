#!/usr/bin/env python
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_KEY = '91&3j(+hkf)$i4-3&g4y!@gp6062nk$$19go)2xv#xlh5*=m*y'

# ALLOWED_HOSTS = ['*']

DEBUG = True

# Application definition
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend', )
ANONYMOUS_USER_ID = -1

INSTALLED_APPS = (
    'django.contrib.admin', 'django.contrib.auth', 'django.contrib.sites',
    'django.contrib.contenttypes', 'django.contrib.sessions',
    'django.contrib.messages', 'django.contrib.staticfiles', 'django_nose',
    'rest_framework', 'rest_framework.authtoken', 'rest_auth', 'apps.article',
    'imagekit', 'pagedown', 'allauth', 'allauth.account',
    'allauth.socialaccount', 'allauth.socialaccount.providers.weibo',
    'allauth.socialaccount.providers.weixin',
    'allauth.socialaccount.providers.github', 'corsheaders', 'taggit')

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'article.sqlite3')
    }
}
# import sys
# if 'test' in sys.argv:
#     DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}

REST_FRAMEWORK = {
    # Use Django's standard 'django.contrib.auth' permissions ,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_AUTHENTICATION_CLASSES':
    ('rest_framework.authentication.TokenAuthentication', ),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.AllowAny', ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': "%Y-%m-%d",
}

BOOTSTRAP_ADMIN_SIDEBAR_MENU = True

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware', )

ROOT_URLCONF = 'conf.urls'

WSGI_APPLICATION = 'conf.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates').replace('\\', '/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'string_if_invalid': 'INVALID: "%s"',
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

USE_TZ = False
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

LOGIN_REDIRECT_URL = '/'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.sina.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'drinksober@sina.com'
EMAIL_HOST_PASSWORD = 'drinks1993'
SERVER_EMAIL = 'drinksober@sina.com'

SITE_ID = 1

STATIC_URL = '/statics/'
STATIC_ROOT = os.path.join(BASE_DIR, 'statics')
STATICDIR = os.path.join(BASE_DIR, 'static/dist')
STATICFILES_DIRS = [STATICDIR]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(STATICDIR, 'media')

WKHTMLTOPDF_CMD = '/usr/bin/wkhtmltopdf'

# CORS_ORIGIN_WHITELIST = (
#     '127.0.0.1:8080',
# )
CORS_ORIGIN_ALLOW_ALL = True

from functools import partial
from ipdb import set_trace
import builtins
trace = partial(set_trace, context=40)
builtins.trace = trace
