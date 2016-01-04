#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: drinks
# @Date:   2016-01-04 15:14:13
# @Last Modified by:   drinks
# @Last Modified time: 2016-01-04 17:55:25


def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return ["Hello World"] # python2
