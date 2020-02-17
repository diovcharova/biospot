from django.test import TestCase
from .models import Category, Producer, Product


class TestCategoryModel(TestCase):

    def test_str(self):
        test_name = Category(category='a category')
        self.assertEqual(str(test_name), 'a category')


class TestProducerModel(TestCase):

    def test_str(self):
        test_name = Producer(producer='a producer')
        self.assertEqual(str(test_name), 'a producer')


class TestProductModel(TestCase):

    def test_str(self):
        test_name = Product(name='a product')
        self.assertEqual(str(test_name), 'a product')

    def test_product_name_max_length(self):
        product = Product(name="a product")
        max_length = product._meta.get_field('name').max_length
        self.assertEquals(max_length, 254)

    def test_can_create_product_with_name_and_price(self):
        product = Product(name="a product", price=1.99)
        self.assertEquals(product.name, "a product")
        self.assertEquals(product.price, 1.99)
