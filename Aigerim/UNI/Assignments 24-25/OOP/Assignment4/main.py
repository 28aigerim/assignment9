from user import User
from user_service import UserService
from user_util import UserUtil


if __name__ == '__main__':
    user1 = User(256895786, 'Aibek', 'Karypov', '2005-12-14')
    user1.email = UserUtil.generate_email(user1.name, user1.surname, 'mail')
    print(user1.email)

    print(UserUtil.validate_email('aibek.karypov@mail.kg'))