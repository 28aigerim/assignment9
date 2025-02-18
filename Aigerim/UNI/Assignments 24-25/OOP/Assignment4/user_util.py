import numpy as np
import random
import string

from user_service import UserService

class UserUtil:
    @staticmethod
    def generate_user_id():
        user_id = int('25' + str(np.random.randint(1000000, 9999999)))
        if user_id != UserService.users.keys():
            return user_id
        else:
            while user_id == UserService.users.keys():
                user_id = int('25' + str(np.random.randint(1000000, 9999999)))
            return user_id

    @staticmethod
    def generate_password():
        length = np.random.randint(8, 20)
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbol = string.punctuation

        all_s = lower + upper + num + symbol
        temp = random.sample(all_s, length)

        password = ''.join(temp)
        return password

    @staticmethod
    def is_strong_password(password):
        password = str(password)

        lower_count = 0
        upper_count = 0
        num_count = 0
        symbol_count = 0

        for sym in password:
            if sym in string.ascii_lowercase:
                lower_count += 1
            elif sym in string.ascii_uppercase:
                upper_count += 1
            elif sym in string.digits:
                num_count += 1
            elif sym in string.punctuation:
                symbol_count += 1

        if lower_count >= 1 and upper_count >= 1 and num_count >= 1 and symbol_count >= 1\
                and len(password) >= 8:
            return 'The password is strong.'
        else:
            return 'The password is weak. Try to create a new one.'

    @staticmethod
    def generate_email(name, surname, domain):
        email = str.lower(name) + '.' + str.lower(surname) + '@' + domain + '.kg'
        return email

    @staticmethod
    def validate_email(email):
        dot = 0
        dog = 0
        kg = 0

        for sym in email:
            if sym == ".":
                dot += 1
            elif sym == "@":
                dog += 1
        if email[-3:] == '.kg':
            kg += 1


        if  dot == 2 and dog == 1 and kg == 1:
            return 'The email is valid.'
        else:
            return 'The email is invalid.'
