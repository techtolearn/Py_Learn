#Reference : https://www.youtube.com/watch?v=RSl87lqOXDE&index=4&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
#program : Inheritance
class employee:

    rais_amt = 1.04
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_Raise(self):
         self.pay = self.pay + employee.rais_amt

    @classmethod
    def set_raisAmount(cls,amount):
        cls.rais_amt = amount

    @classmethod
    def string_emp(cls,emp_str):
     first,last,pay  = emp_str.split('-')
     return cls(first,last,pay)

class developer(employee):

    def __init__(self,first,last,pay,pro_name):
        super().__init__(first,last,pay)
        self.pgm = pro_name


class manager(employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None :
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('-->',emp.fullname())




dev1 =developer("Tavi","satheesh",5412000,"java_advanced")
dev2 =developer("Deexith","kumar",6542810,"Python")

print("******Developer example1*********")
print(dev1.pay)
dev1.apply_Raise()
print(dev1.pay)
print("\n")

print("******Developer example2*********")
print(dev1.email)
print(dev2.fullname())
print(dev1.pgm)
print("\n")

print("******Manager example1*********")

mgr1 = manager('Anshuman','dadich',3212132,[dev1])
mgr2 = manager('Pritesh','Natesan',8932132,[dev2])

print(mgr1.email)
print(mgr2.fullname())

mgr1.print_emp()
print("\n")

print("******Manager example2*********")
mgr1.add_emp(dev1)
mgr1.add_emp(dev2)
mgr1.print_emp()
print("\n")

print("******Manager removed employees*********")
mgr1.rem_emp(dev1)
mgr1.print_emp()
# print(emp1.email)
# print(employee.fullname(emp1))
# print(emp1.fullname())
#
# emp_str1 = employee.string_emp("Tavi-satheesh-5412000")
# emp_str2 = employee.string_emp("Deexith-kumar-6542810")
#
# print(emp_str1.fullname())
# emp_str2.set_raisAmount(1.25)
# print(employee.rais_amt)

