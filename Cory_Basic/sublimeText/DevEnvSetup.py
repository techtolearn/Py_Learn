# https://www.youtube.com/watch?v=xFciV6Ew5r4&index=10&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU

#https://www.youtube.com/watch?v=xqcTfplzr7c&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=62
# Setting up a Python Development Environment in Sublime Text
# https://www.youtube.com/watch?v=DjEuROpsvp4&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=11
# Setting up a Python Development Environment in Atom

import sys

print(sys.executable)
print(sys.version)

class Employee:
    def __init__(self,first,last):
         self.first = first
         self.last = last

    def test_method(self):
        pass

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)

    @property
    def fullname(self):
         return '{} {}'.format(self.first,self.last)

emp1 = Employee('Satheesh','kumar')

print(emp1)
print(emp1.email)
print(emp1.fullname)
