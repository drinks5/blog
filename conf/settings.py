#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: drinks
# @Date:   2015-12-22 16:01:28
# @Last Modified by:   drinksober
# @Last Modified time: 2016-04-26 11:36:53

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '91&3j(+hkf)$i4-3&g4y!@gp6062nk$$19go)2xv#xlh5*=m*y'

# SECURITY WARNING: don't run with debug turned on in production!


# ALLOWED_HOSTS = ['*']
# from .production import *

DEBUG = True

# bootstrap
DAB_FIELD_RENDERER = 'django_admin_bootstrapped.renderers.BootstrapFieldRenderer'

from django.contrib import messages
"""
bootstrap alert info...
"""
MESSAGE_TAGS = {
    messages.SUCCESS: 'alert-success success',
    messages.WARNING: 'alert-warning warning',
    messages.ERROR: 'alert-danger error'
}

# Application definition


# AUTHENTICATION_BACKENDS = (
#    'userena.backends.UserenaAuthenticationBackend',
#    'guardian.backends.ObjectPermissionBackend',
 #   'django.contrib.auth.backends.ModelBackend',
#)
ANONYMOUS_USER_ID = -1


INSTALLED_APPS = (
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_nose',
    'rest_framework',
    'apps.accounts',
    'apps.article',
    'apps.wechat',
)
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
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS

BOOTSTRAP_ADMIN_SIDEBAR_MENU = True


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    # 'django.middleware.csrf.CsrfResponseMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

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



# DATABASES = {
#     'default': {
#         'ENGINE' : 'django.db.backends.mysql',
#         'NAME'    : 'article',
#         'USER'     : 'root',
#         'PASSWORD'  : '123456',
#         'HOST'   : '',
#         'PORT'   : '3306',
#     }
#     }
USE_TZ = False
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'


USE_I18N = True

USE_L10N = True


#AUTH_PROFILE_MODULE = 'accounts.MyProfile'

#LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
#LOGIN_URL = '/accounts/signin/'
#LOGOUT_URL = '/accounts/signout/'
LOGIN_REDIRECT_URL = '/'
# AUTH_USER_MODEL = 'accounts.User'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.sina.com'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'drinksober@sina.com'
EMAIL_HOST_PASSWORD = 'drinks1993'
SERVER_EMAIL = 'drinksober@sina.com'
#DEFAULT_FROM_EMAIL = 'drinksober@sina.com'

SITE_ID = 2

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/statics/'
STATIC_ROOT = os.path.join(BASE_DIR,'statics')
STATICDIR= os.path.join(BASE_DIR,'static/dist')
STATICFILES_DIRS = [STATICDIR,]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(STATICDIR, 'media')
