from django.test.client import Client
from django.test import TestCase


class BaseTestCase(TestCase):
    def setUp(self):
        self.c = c = Client()
        self.GET = c.get
        self.POST = c.post
