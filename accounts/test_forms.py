from django.test import TestCase
from django.contrib.auth.models import User


class TestUserLogInForm(TestCase):

    def setUp(self):
        User.objects.create_user('temporary', 'temporary')
