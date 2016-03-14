# -*- coding: utf-8 -*-
# @Author: drinks
# @Date:   2016-03-09 17:43:18
# @Last Modified by:   drinks
# @Last Modified time: 2016-03-10 11:57:56

import hashlib
import simplejson
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseServerError, Http404
from django.views.generic import View
from django.core.urlresolvers import reverse
from django.conf import settings

from .models import User
from .serializers import UserSerializer
from .auth_view import AuthView as BaseView
from .wechat_api import WechatApi, wx_log_error
from youhui.utils import log_err

# Create your views here.



class WecahtApiView(View):

    # 填入公众号appid, appsecret
    APPID = settings.APPID
    APPSECRET = settings.APPSECRET
    HOST = settings.HOST

    wechat_api = WechatApi(appid=APPID, appsecret=APPSECRET)


class WxSignature(View):
      pass #非重点省略

class AuthView(WecahtApiView):
    def get(self, request):

        path = request.GET.get('path')
        if path:
            if 'user' in request.session:
                return redirect(path)
            else:
                red_url = '%s%s?path=%s' % (self.HOST, reverse('wx:get_user_info'), path)
                redirect_url = self.wechat_api.auth_url(red_url)

                print('auth_url', redirect_url)
                return redirect(redirect_url)
        else:
            return Http404('parameter path not founded!')



class GetUserInfoView(WecahtApiView):
    def get(self, request):

        redir_url = request.GET.get('path')
        code = request.GET.get('code')

        if redir_url and code:

            # 获取网页授权access_token
            token_data, error = self.wechat_api.get_auth_access_token(code)

            if error:
                wx_log_error(error)
                return HttpResponseServerError('get access_token error')

            # 获取用户信息信息
            user_info, error = self.wechat_api.get_user_info(
                token_data['access_token'], token_data['openid'])

            if error:
                wx_log_error(error)
                return HttpResponseServerError('get userinfo error')

            # 存储用户信息
            user = self._save_user(user_info)
            if not user:
                return HttpResponseServerError('save userinfo error')

            # 用户对象存入session
            request.session['user'] = user

            # 跳转回目标页面
            return redirect(redir_url)

        # 用户禁止授权后怎么操作
        else:
            return Http404('parameter path or code not founded!!')

    def _save_user(self, data):
        user = User.objects.filter(openid=data['openid'])

        # 没有则存储用户数据，有返回用户数据的字典
        if 0 == user.count():
            user_data = {
                'nick': data['nickname'].encode('iso8859-1').decode('utf-8'),
                'openid': data['openid'],
                'avatar': data['headimgurl'],
                'info': self._user2utf8(data),
            }

            if 'unionid' in data:
                user_data.update('unionid', data.unionid)

            try:
                new_user = User(**user_data)
                new_user.save()

                user_data.update({'id': new_user.id})

                return user_data
            except Exception, e:
                log_err(e)

            return None
        else:
            # 把User对象序列化成字典，具体看rest_framework中得内容
            return UserSerializer(user[0]).data


    # 解决中文显示乱码问题
    def _user2utf8(self, user_dict):
        utf8_user_info = {
            "openid": user_dict['openid'],
            "nickname": user_dict['nickname'].encode('iso8859-1').decode('utf-8'),
            "sex": user_dict['sex'],
            "province": user_dict['province'].encode('iso8859-1').decode('utf-8'),
            "city": user_dict['city'].encode('iso8859-1').decode('utf-8'),
            "country": user_dict['country'].encode('iso8859-1').decode('utf-8'),
            "headimgurl": user_dict['headimgurl'],
            "privilege": user_dict['privilege'],
        }

        if 'unionid' in user_dict:
            utf8_user_info.update({'unionid': user_dict['unionid']})

        return utf8_user_info


class TestView(BaseView):
    def get(self, request):

        return render(request, 'test.html')
