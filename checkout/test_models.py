from django.test import TestCase
from .models import Order, OrderLineItem
from products.models import Product


class TestOrderModel(TestCase):

    def test_str(self):
        test_str = Order(id='1', date="feb 2020", full_name="John")
        self.assertEqual(str(test_str), '{0}-{1}-{2}'.format(1, "feb 2020", "John"))


class TestOrderLineItemModel(TestCase):

    def test_str(self):
        product = Product(name="product", price="1.99")
        test_str = OrderLineItem(quantity='1', product=product)
        self.assertEqual(str(test_str), '{0} {1} @ {2}'.format(1, "product", "1.99"))

    def test_total(self):
        product = Product(name="product", price=1.99)
        orderlineitem = OrderLineItem(quantity=1, product=product)
        self.assertEqual(orderlineitem.total(), 1.99)