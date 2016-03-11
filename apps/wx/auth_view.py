# -*- coding: utf-8 -*-
# @Author: drinks
# @Date:   2016-03-09 18:26:32
# @Last Modified by:   drinks
# @Last Modified time: 2016-03-09 18:27:01

import urllib

from django.views.generic import View
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

class AuthView(View):

    def dispatch(self, request, *args, **kwargs):
        # 判断是否有授权
        if not 'user' in request.session:
            # 用户需要访问的url路径
            path = request.get_full_path()

            # 跳转url,
            red_url = '%s?path=%s' % (reverse('wx_auth'), urllib.quote(path))
            return redirect(red_url)

        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        return handler(request, *args, **kwargs)
