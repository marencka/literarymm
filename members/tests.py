# Written by Emily Pumer
from atexit import register
from django.test import TestCase, Client
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from members.views import login_user, register_user, sign_up_start, signupCont


# URL tests for members/urls.py:
# 4 tests in total

class TestUrls(SimpleTestCase):
    def test_loginuser_url_resolves(self):
        url = reverse('log_in')
        self.assertEquals(resolve(url).func, login_user)
    
    def test_registeruser_url_resolves(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register_user)
    
    def test_signupstart_url_resolves(self):
        url = reverse('sign_up_start')
        self.assertEquals(resolve(url).func, sign_up_start)

    def test_signupcont_url_resolves(self):
        url = reverse('signupCont')
        self.assertEquals(resolve(url).func, signupCont)






