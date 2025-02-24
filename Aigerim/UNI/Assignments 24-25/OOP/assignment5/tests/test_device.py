import unittest
from device import Device


class TestDevice(unittest.TestCase):

    def test_display_info(self):
        device1 = Device('Iphone 15', 120, 3, 12)
        self.assertEqual(device1.display_info(), 'Device Iphone 15 with price 120, stock: 3, warranty period: 12 months.',
                         'Something wrong.')

    def test_is_available(self):
        device1 = Device('Iphone 15', 120, 3, 12)
        self.assertEqual(device1.is_available(1), True, 'Something wrong.')

