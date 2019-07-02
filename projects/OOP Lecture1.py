#Python Object-Oriented Programming


class Employee:

    num_of_emp = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower()  + '@paltreev.com'

        Employee.num_of_emp += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)\

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

print(Employee.num_of_emp)

emp_1 = Employee('Dubem', 'Oguji', 50000)
emp_2 = Employee('Josemaria', 'Nriagu', 60000)

'''print(emp_1.__dict__)
print(emp_2.__dict__)
print(Employee.__dict__)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)'''

print(Employee.num_of_emp)

'''print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)'''

import datetime
my_date = datetime.date(2017, 5, 15)

print(Employee.is_workday(my_date))