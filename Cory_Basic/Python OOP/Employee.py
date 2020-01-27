#class - instance variable
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=40
class employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first +'.'+last+'@gmail.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp1 = employee("Saheesh","kumar",1500000)
emp2 = employee("Divya","satheesh",2000000)

print(emp1.first)
print(emp2.email)
print("\n")

print(emp1.fullname())   #we areusing object and calling method
print(employee.fullname(emp2))  #we use method throug class

