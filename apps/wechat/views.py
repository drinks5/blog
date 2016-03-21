# -*- coding: utf-8 -*-
# @Author: drinks
# @Date:   2016-03-21 21:17:50
# @Last Modified by:   drinks
# @Last Modified time: 2016-03-21 21:44:34

import hashlib

from django.shortcuts import render
from django.http import HttpResponse

TOKEN = 'linlin'
# Create your views here.

def tokenView(request):
    if request.method == "GET":
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
        token = TOKEN
        tmp_list = [token, timestamp, nonce]
        tmp_list.sort()
        tmp_str = "%s%s%s" % tuple(tmp_list)
        tmp_str = hashlib.sha1(tmp_str).hexdigest()
        if tmp_str == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("weixin  index")

def check_signature(signature, timestamp, nonce):
    L = [timestamp, nonce, token]
    L.sort()
    s = L[0] + L[1] + L[2]
    return hashlib.sha1(s).hexdigest() == signature
