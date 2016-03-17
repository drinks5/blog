# -*- coding: utf-8 -*-
# @Author: drinks
# @Date:   2016-03-15 16:24:00
# @Last Modified by:   drinks
# @Last Modified time: 2016-03-17 15:50:01
"""
WSGI config for blog_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""
import os, sys
sys.path.append('/home/linlin/Desktop/blog/lib/python2.7/site-packages')
sys.path.append('/home/linlin/Desktop/blog/blog')
sys.path.append('/home/linlin/Desktop/blog/blog/conf')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "conf.settings")

application = get_wsgi_application()
