from user import User


class UserService:
    users = {}

    @classmethod
    def add_user(cls, user):
        if user.user_id not in cls.users.keys():
            cls.users[user.user_id] = user
            return 'Successfully added new user. '
        else:
            return 'Such user ID already exists, try again. '


    @classmethod
    def find_user(cls, user_id):
        if user_id in cls.users.keys():
            return f'User: {cls.users[user_id].get_details()}'
        else:
            return 'User is not found.'

    @classmethod
    def delete_user(cls, user_id):
        if user_id in cls.users.keys():
            cls.users.pop(user_id, None)
            return 'Successfully deleted the user.'
        else:
            return 'No such user.'

    @classmethod
    def update_user(cls, user_id, user_update):
        if user_id in cls.users.keys():
            cls.users[user_id] = user_update
            return 'User ID successfully updated. '
        else:
            return 'No such user_id.'

    @classmethod
    def get_number(cls):
        return f'Number of students: {len(cls.users.keys())}.'