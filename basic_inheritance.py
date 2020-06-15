class Employee:

    def __init__(self, first, last, pay):  # constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)


class Developer(Employee):      # inherit from employee class
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

# print(help(Developer))

dev_1 = Developer('ani', 'amir', 300, 'python')
dev_2 = Developer('bob', 'rob', 300, 'java')


class Manager(Employee):
    def __init__(self, first, last, pay, employees  = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


mgr = Manager('sue', 'smith', 9000, [dev_1])

print(mgr.email)
mgr.add_emp(dev_2)
mgr.remove_emp(dev_1)
mgr.print_emps()

print(isinstance(mgr, Manager))         # check its instance
print(issubclass(Developer, Employee))  # check if its subclass
 