#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: root
# @Date:   2015-12-30 16:27:44
# @Last Modified by:   drinks
# @Last Modified time: 2015-12-30 18:50:41

import os
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
print(PROJECT_DIR)
print(os.path.join(PROJECT_DIR, "static"))
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
print(STATIC_ROOT)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
