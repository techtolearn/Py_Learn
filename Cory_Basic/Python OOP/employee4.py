#Ref-https://www.youtube.com/watch?v=3ohzBxoFHAY&index=5&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc
#pgm using Dunder/magic method

class employee:

    raisAmt =1.05
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay =self.pay + self.raisAmt

    def __repr__(self):  #dunder method
         return '{} {} {}'.format(self.first,self.last,self.pay)  #when type print emp1 - it automatically print defined attr values

    def __str__(self): #dunder method
        return '{} {}'.format(self.fullname(),self.email) #when type print emp1 - it automatically print defined attr values
    def __add__(self): #dunder method
        return (emp1.pay + emp2.pay)

emp1 =employee("Tavi","satheesh",5412000)
emp2 =employee("Deexith","kumar",6542810)


print(emp1)
print(emp1.__add__())

