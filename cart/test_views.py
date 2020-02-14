from django.urls import reverse
from django.test import TestCase


class TestCartView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('view_cart'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('view_cart'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')
