from django.test import TestCase
from django.urls import reverse


class TestAllproductsView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')


class TestSkincareproductsView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/products/skincare/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('skincare'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('skincare'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products_skincare_and_beauty.html')


class TestBulkproductsView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/products/bulk/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('bulk'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('bulk'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products_bulk.html')


class TestCleaningproductsView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/products/cleaning/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('cleaning'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('cleaning'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products_cleaning_and_household.html')


class TestOrganicproductsView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/products/organic/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('organic'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('organic'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products_organic.html')


class TestSupplementproductsView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/products/supplements/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('supplements'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('supplements'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products_supplements.html')


class TestRawproductsView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/products/raw/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('raw'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('raw'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products_raw_and_superfoods.html')
