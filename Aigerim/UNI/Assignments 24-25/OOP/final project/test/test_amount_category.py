import unittest
from category_amount import CategoryAmount


class TestCategoryAmount(unittest.TestCase):
    def test_amount_error(self):
        cat_amount1 = CategoryAmount("Food", 100)
        self.assertEqual(cat_amount1.amount_error(), None, "Error")

    def test_str(self):
        cat_amount1 = CategoryAmount("Food", 100)
        self.assertEqual(cat_amount1.__str__(), f'Category: Food\n'
                f'Amount: 100', "Error")