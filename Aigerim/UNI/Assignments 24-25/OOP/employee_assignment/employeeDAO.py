import sqlite3
from entity_class import Employee


class EmployeeDAO:
    def __init__(self, databasefile):
        self.conn = sqlite3.connect(databasefile)
        self.cursor = self.conn.cursor()

    def get_by_id(self, search_id):
        sql = '''
            SELECT id, name, position, salary, hire_date
            FROM Employee
            WHERE id = ?
        '''
        self.cursor.execute(sql, (search_id,))

        row = self.cursor.fetchone()
        if row:
            employee = Employee(id=row[0], name=row[1], position=row[2],salary=row[3], hire_date=row[4])
        else:
            employee = None

        return employee

    def get_all(self):
        sql = '''
            SELECT * FROM Employee 
            ORDER BY name ASC
        '''
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()

        employees = []

        for row in rows:
            employee = Employee(id=row[0], name=row[1], position=row[2], salary=row[3], hire_date=row[4])
            employees.append(employee)

        return employees

    def insert(self, e: Employee):
        sql = '''
            INSERT INTO Employee (name, position, salary, hire_date)
            VALUES (?, ?, ?, ?)
        '''
        self.cursor.execute(sql, (e.name, e.position, e.get_salary(), e.hire_date))
        id = self.cursor.lastrowid
        self.conn.commit()

        return id

    def update(self, e: Employee):
        sql = '''
            UPDATE Employee
            SET name = ?, position = ?, salary = ?, hire_date = ?
            WHERE id = ?
        '''
        self.cursor.execute(sql, (e.name, e.position, e.get_salary(), e.hire_date, e.id))
        self.conn.commit()
        return self.cursor.rowcount

    def delete(self, id):
        sql = '''
            DELETE FROM Employee
            WHERE id = ?
        '''
        self.cursor.execute(sql, (id,))
        self.conn.commit()

        return self.cursor.rowcount

