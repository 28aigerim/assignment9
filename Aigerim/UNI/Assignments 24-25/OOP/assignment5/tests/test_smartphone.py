import unittest
from smartphone import Smartphone


class TestSmartphone(unittest.TestCase):

    def test_display_info(self):
        smartphone1 = Smartphone('Iphone', 10, 2, 12, 5, 100)
        self.assertEqual(smartphone1.display_info(),
                         'Device Iphone with price 10, stock: 2, warranty period: 12 months.Smartphone with screen size: 5 and battery life: 100.',
                         'Something wrong.'
                         )

    def test_make_call(self):
        smartphone1 = Smartphone('Iphone', 10, 2, 12, 5, 100)
        self.assertEqual(smartphone1.make_call(),
                         'You are making a call.',
                         'Something wrong.')

    def test_install_app(self):
        smartphone1 = Smartphone('Iphone', 10, 2, 12, 5, 100)
        self.assertEqual(smartphone1.install_app(),
                         'You are installing app.',
                         'Something wrong.')