from django.test import TestCase
from django.urls import reverse
from home.forms import ContactForm


class TestHomepageView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class TestContactsView(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/home/contacts/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('contacts'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('contacts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contacts.html')

    def test_invalid_data(self):
        form = ContactForm({"name": "Test", "body": "Test message"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['contact_email'], [u'This field is required.'])

    def test_valid_form(self):
        data = dict(
            contact_name='test',
            contact_email='test@test.com',
            content='test message from user foo',
        )
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())
