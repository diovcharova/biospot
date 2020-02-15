from django.apps import apps
from django.test import TestCase
from cart.apps import CartConfig


class TestCartConfig(TestCase):
    def test_apps(self):
        self.assertEqual(CartConfig.name, 'cart')
        self.assertEqual(apps.get_app_config('cart').name, 'cart')
