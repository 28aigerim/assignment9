import unittest

from user_util import UserUtil


class TestUserUtil(unittest.TestCase):

    def test_generate_user_id(self):
        self.assertEqual(len(UserUtil.generate_user_id()), 9, 'Something wrong.')
        self.assertEqual(UserUtil.generate_user_id() // 10000000, 25,
                         'Something wrong.')

    def test_generate_password(self):
        self.assertLessEqual(len(UserUtil.generate_password()), 20,
                             'Something wrong.')

    def test_is_strong_password(self):
        self.assertEqual(UserUtil.is_strong_password("AibekKar1?"),
                         'The password is strong.',
                         'Something wrong.')


    def test_generate_email(self):
        self.assertEqual(UserUtil.generate_email('Aibek', 'Karypov', 'mail'),
                         'aibek.karypov@mail.kg',
                         'Something wrong. ')


    def test_validate_email(self):
        self.assertEqual(UserUtil.validate_email('aibek.karypov@mail.kg'),
                         'The email is valid.',
                         'Something wrong.')