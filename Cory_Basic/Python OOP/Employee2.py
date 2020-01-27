#reference : https://www.youtube.com/watch?v=rq8cL2XMM5M&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=3
#pgm : regular method|class method |static method

class employee:

    emp_num = 0
    raise_amt = 1.05
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

    @classmethod
    def set_raise_amt(cls,amont):  #this is class method and cls is like self here
        cls.raise_amt = amont
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() ==6:
            return  False
        return True




emp1 =employee("Tavi","satheesh",5412000)
emp2 =employee("Deexith","kumar",6542810)

print("Class method example 1")
print("======================")
print(employee.raise_amt)
employee.set_raise_amt(1.06)
print(employee.raise_amt)

print("Class method example 2")
print("======================")
emp1_str = employee.from_string("Jose-Boltron-5012000")
emp2_str = employee.from_string("Satheesh-Kumar-3652100")
print(emp1_str.email)
print(emp2_str.fullname())

print("Static method example 1")
print("=======================")
import  datetime
my_date = datetime.date(2016, 7, 10)
print(employee.is_workday(my_date))
