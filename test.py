# -*- coding: utf-8 -*-
# @Author: linlin
# @Date:   2016-03-09 13:07:53
# @Last Modified by:   drinks
# @Last Modified time: 2016-03-17 11:26:00

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return ["Hello World"] # python2
    #return [b"Hello World"] # python3
