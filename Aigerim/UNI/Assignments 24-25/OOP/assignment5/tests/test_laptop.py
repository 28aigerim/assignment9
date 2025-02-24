import unittest
from laptop import Laptop


class TestLaptop(unittest.TestCase):

    def test_display_info(self):
        laptop1 = Laptop('HP', 120000, 9, 12, 32, 4.8)
        self.assertEqual(laptop1.display_info(),
                         'Device HP with price 120000, stock: 9, warranty period: 12 months.Laptop with RAM size: 32 and processor speed: 4.8.',
                         'Something wrong.'
                         )

    def test_run_program(self):
        laptop1 = Laptop('HP', 120000, 9, 12, 32, 4.8)
        self.assertEqual(laptop1.run_program(),
                         'You are running a program.',
                         'Something wrong.')

    def test_use_keyboard(self):
        laptop1 = Laptop('HP', 120000, 9, 12, 32, 4.8)
        self.assertEqual(laptop1.use_keyboard(),
                         'You are using a keyboard.',
                         'Something wrong.')