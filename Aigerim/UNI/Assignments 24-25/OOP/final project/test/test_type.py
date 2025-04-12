import unittest
from type import Type


class TestType(unittest.TestCase):
    def test_amount_error(self):
        type1 = Type("Expense", 100)
        self.assertEqual(type1.amount_error(), None, "Error")

    def test_str(self):
        type1 = Type("Expense", 100)
        self.assertEqual(type1.__str__(), f'Type: Expense, amount: 100.')