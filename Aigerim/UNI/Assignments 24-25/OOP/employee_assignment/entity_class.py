class Employee:
    def __init__(self, id, name, position, salary, hire_date):
        self.id = id
        self.name = name
        self.position = position
        self.__salary = salary
        self.hire_date = hire_date

    def __str__(self):
        return f'Employee id: {self.id}, name: {self.name}, position: {self.position}.'

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary
