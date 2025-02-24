import unittest
from tablet import Tablet


class TestTablet(unittest.TestCase):

    def test_display_info(self):
        tablet1 = Tablet('Ipad', 10, 10, 12, '1020x720', 0.4)
        self.assertEqual(tablet1.display_info(),
                         'Device Ipad with price 10, stock: 10, warranty period: 12 months.Tablet with screen resolution: 1020x720 and weight: 0.4 kg.',
                         'Something wrong.'
                         )

    def test_browse_internet(self):
        tablet1 = Tablet('Ipad', 10, 10, 12, '1020x720', 0.4)
        self.assertEqual(tablet1.browse_internet(),
                         'You are browsing internet.',
                         'Something wrong.')

    def test_use_touchscreen(self):
        tablet1 = Tablet('Ipad', 10, 10, 12, '1020x720', 0.4)
        self.assertEqual(tablet1.use_touchscreen(),
                         'You are using touchscreen.',
                         'Something wrong.')

