import unittest
from cart import Cart


class TestCart(unittest.TestCase):

    def test_get_total_price(self):
        self.assertEqual(Cart.get_total_price(), 'The total price in the cart is 0 soms.', 'Something wrong.')

