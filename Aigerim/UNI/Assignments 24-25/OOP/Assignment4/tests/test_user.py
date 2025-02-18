import unittest

from user import User


class TestUser(unittest.TestCase):

    def test_get_details(self):
        user1 = User(256895786, 'Aibek', 'Karypov', '2005-12-14')
        self.assertEqual(user1.get_details(),
                         "User Aibek Karypov with ID: 256895786.",
                         'Something wrong')

    def test_get_age(self):
        user1 = User(256895786, 'Aibek', 'Karypov', '2005-12-14')
        self.assertEqual(user1.get_age(),
                         "User's age: 19", 'Something wrong')
