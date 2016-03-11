# -*- coding: utf-8 -*-
# @Author: drinks
# @Date:   2016-03-09 18:25:36
# @Last Modified by:   drinks
# @Last Modified time: 2016-03-09 18:25:41

import requests
import simplejson
import urllib
import logging

log = logging.getLogger('django')

class APIError(object):
    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

def wx_log_error(APIError):
    log.error('wechat api error: [%s], %s' % (APIError.code, APIError.msg))

class WechatBaseApi(object):

    API_PREFIX = u'https://api.weixin.qq.com/cgi-bin/'

    def __init__(self, appid, appsecret, api_entry=None):
        self.appid = appid
        self.appsecret = appsecret
        self._access_token = None
        self.api_entry = api_entry or self.API_PREFIX

    @property
    def access_token(self):
        if not self._access_token:
            token, err = self.get_access_token()

            if not err:
                self._access_token = token['access_token']
                return self._access_token
            else:
                return None

        return self._access_token


    # 解析微信返回的json数据，返回相对应的dict
    def _process_response(self, rsp):
        if 200 != rsp.status_code:
            return None, APIError(rsp.status_code, 'http error')
        try:
            content = rsp.json()

        except Exception:
            return None, APIError(9999, 'invalid response')
        if 'errcode' in content and content['errcode'] != 0:
            return None, APIError(content['errcode'], content['errmsg'])

        return content, None


    def _get(self, path, params=None):
        if not params:
            params = {}

        params['access_token'] = self.access_token

        rsp = requests(self.api_entry + path, params=params)

        return self._process_response(rsp)


    def _post(self, path, data, type='json'):

        header = {'content-type': 'application/json'}

        if '?' in path:
            url = self.api_entry + path + 'access_token=' + self.access_token
        else:
            url = self.api_entry + path + '?' + 'access_token=' + self.access_token

        if 'json' == type:
            data = simplejson.dumps(data, ensure_ascii=False).encode('utf-8')

        rsp = requests.post(url, data, headers=header)

        return self._process_response(rsp)



class WechatApi(WechatBaseApi):

    def get_access_token(self, url=None, **kwargs):
        params = {'grant_type': 'client_credential', 'appid': self.appid, 'secret': self.appsecret}

        if kwargs:
            params.update(kwargs)

        rsp = requests.get(url or self.api_entry + 'token', params)

        return self._process_response(rsp)

    #返回授权url
    def auth_url(self, redirect_uri, scope='snsapi_userinfo', state=None):
        url = 'https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s&redirect_uri=%s&response_type=code&scope=%s&state=%s#wechat_redirect' % \
              (self.appid, urllib.quote(redirect_uri), scope, state if state else '')
        return url

   # 获取网页授权的access_token
    def get_auth_access_token(self, code):
        url = u'https://api.weixin.qq.com/sns/oauth2/access_token'
        params = {
            'appid': self.appid,
            'secret': self.appsecret,
            'code': code,
            'grant_type': 'authorization_code'
        }

        return self._process_response(requests.get(url, params=params))

    # 获取用户信息
    def get_user_info(self, auth_access_token, openid):
        url = u'https://api.weixin.qq.com/sns/userinfo?'
        params = {
            'access_token': auth_access_token,
            'openid': openid,
            'lang': 'zh_CN'
        }

        return self._process_response(requests.get(url, params=params))
