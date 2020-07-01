class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def fullname_2(self):
        return self.first + ' ' + self.last


emp_1 = Employee('andrei', 'balanuta', 60000)

print(emp_1.email)

print(emp_1.fullname())
print(emp_1.fullname_2())
