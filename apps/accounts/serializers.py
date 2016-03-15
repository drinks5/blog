# -*- coding: utf-8 -*-
# @Author: drinks
# @Date:   2016-03-09 13:14:06
# @Last Modified by:   drinks
# @Last Modified time: 2016-03-09 17:47:55
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer( serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer( serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name' )

