# -*- coding: utf-8 -*-
"""
Local settings

- Run in Debug mode

- Use console backend for emails

- Add Django Debug Toolbar
- Add django-extensions as app
"""

# Your local stuff: Below this line define 3rd party library settings
# ------------------------------------------------------------------------------
import builtins
import functools

from ipdb import set_trace as _set_trace

from .common import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env('DJANGO_SECRET_KEY',
                 default='bhuqwp@r2g&e(2g)*(3a+kdsy&33_zaj73&l^_b#bf-%)te-x6')

# Mail settings
# ------------------------------------------------------------------------------

EMAIL_PORT = 1025

EMAIL_HOST = 'localhost'
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.console.EmailBackend')

# django-debug-toolbar
# ------------------------------------------------------------------------------
# MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
# INSTALLED_APPS += ('debug_toolbar', )

INTERNAL_IPS = ['127.0.0.1', '0.0.0.0']
# tricks to have debug toolbar when developing with docker

# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ('django_extensions', )

set_trace = functools.partial(_set_trace, context=40)
builtins.trace = set_trace
