import unittest

from user import User
from user_service import UserService


class TestUserService(unittest.TestCase):

    def test_add_user(self):
        user1 = User(256895786, 'Aibek', 'Karypov', '2005-12-14')
        self.assertEqual(UserService.add_user(user1), 'Successfully added new user. ',
                         'Something wrong')


    def test_find_user(self):
        user1 = User(256895786, 'Aibek', 'Karypov', '2005-12-14')
        UserService.add_user(user1)
        self.assertEqual(UserService.find_user(user1.user_id),
                         f'User: {user1}', 'Something wrong.')


    def test_delete_user(self):
        user1 = User(256895786, 'Aibek', 'Karypov', '2005-12-14')
        UserService.add_user(user1)
        self.assertEqual(UserService.delete_user(user1.user_id),
                         'Successfully deleted the user.',
                         'Something wrong. ')


    def test_update_user(self):
        user1 = User(256895786, 'Aibek', 'Karypov', '2005-12-14')
        user_update = User(256895787, 'Aigul', 'Bekenova', '2004-12-14')
        UserService.add_user(user1)
        self.assertEqual(UserService.update_user(user1.user_id, user_update),
                         'User ID successfully updated. ',
                         'Something wrong.')


    def test_get_number(self):
        user1 = User(256895786, 'Aibek', 'Karypov', '2005-12-14')
        UserService.add_user(user1)
        self.assertEqual(UserService.get_number(), 'Number of students: 1.', 'Something wrong.')