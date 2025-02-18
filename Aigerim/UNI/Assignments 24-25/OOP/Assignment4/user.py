from datetime import date
import datetime
import dateutil


class User:

    def __init__(self, user_id, name, surname, birthday, password=0):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.email = name + '.' + surname + '@mail.kg'
        self.__password = password
        self.birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d').date()

    def get_details(self):
        return f'User {self.name} {self.surname} with ID: {self.user_id}.'

    def get_age(self):
        today = date.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return age
