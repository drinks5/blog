# -*- coding: utf-8 -*-
# @Author: drinksober
# @Date:   2016-04-26 11:20:30
# @Last Modified by:   drinksober
# @Last Modified time: 2016-04-26 11:39:00

from django.test import TestCase


class BaseTestCase(TestCase):
    """
    可重写 testcase中的 setUp 方法, 并且继承祖类setUp方法中定义的属性
    """

    @classmethod
    def setUpClass(cls):
        super(BaseTestCase, cls).setUpClass()
        if cls != BaseTestCase and cls.setUp != BaseTestCase.setUp:
            orig_setUp = cls.setUp

            def setUpOverride(self, *args, **kwargs):
                BaseTestCase.setUp(self)
                return orig_setUp(self, *args, **kwargs)

            cls.setUp = setUpOverride

        if cls != BaseTestCase and cls.tearDown != BaseTestCase.tearDown:
            orig_tearDown = cls.tearDown

            def tearDownOverride(self, *args, **kwargs):
                ret_val = orig_tearDown(self, *args, **kwargs)
                BaseTestCase.tearDown(self)
                return ret_val

            cls.tearDown = tearDownOverride
