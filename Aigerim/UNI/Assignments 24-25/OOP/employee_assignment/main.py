from employeeDAO import EmployeeDAO
from entity_class import Employee


if __name__ == "__main__":
    dao = EmployeeDAO('employee.sqlite')

    print(dao.delete(21))