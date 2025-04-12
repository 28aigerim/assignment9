from transaction import Transaction
import unittest


class TestTransaction(unittest.TestCase):
    def test_set_id(self):
        transact1 = Transaction(1, "12-04-25", 100, "Expense", "Food")
        transact1.set_id(2)
        self.assertEqual(transact1.id, 2, "Error")

    def test_amount_error(self):
        transact1 = Transaction(1, "12-04-25", 0, "Expense", "Food")
        self.assertEqual(transact1.amount_error(), "The amount can not be negative or zero", "Error")

    def test_str(self):
        transact1 = Transaction(1, "12-04-25", 100, "Expense", "Food")
        self.assertEqual(transact1.__str__(), f'ID: 1\n'
                f'Date: 12-04-25\n'
                f'Transaction amount: 100\n'
                f'Transaction type: Expense'
                f'Category: Food', "Error")
