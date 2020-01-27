#reference : https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
#Example : class variable

class employee:

    emp_num = 0
    raise_amt = 1.05  #class variables
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@gmail.com'
        employee.emp_num +=1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = self.pay * employee.raise_amt  #you can give as self.raise_amt also


print(employee.emp_num)

emp1 =employee("Tavi","satheesh",5412000)
emp2 =employee("Deexith","kumar",6542810)

print(employee.raise_amt)
print(emp1.raise_amt)
print("\n")

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print("\n")

print(employee.emp_num)



