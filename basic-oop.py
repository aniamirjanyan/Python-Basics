import datetime


class Employee:
    num_of_employees = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):  # constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# you can input manually
# emp_1 = Employee()
# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'corey@company.com'
# emp_1.pay = 50000


# or (instances)
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Ani', 'Amir', 60000)

print(emp_1.fullname())
# same here
print(Employee.fullname(emp_1))

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.__dict__)  # object attributes

Employee.raise_amount = 1.05
print(emp_1.raise_amount)

print(Employee.num_of_employees)  # gives 2 after creating 2

Employee.set_raise_amt(1.05)  # suing class method - setting the amount

# - - - - - -
emp_str_1 = 'John-Doe-40000'
new_emp_1 = Employee.from_str(emp_str_1)

my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))
