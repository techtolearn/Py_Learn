'''
https://www.youtube.com/watch?v=pd-0G0MigUA&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=51
Python SQLite Tutorial: Complete Overview - Creating a Database, Table, and Running Queries
'''

class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)

    @property
    def fulname(self):
        return '{} {}'.format(self.first,self.last)

    def __repr__(self):
        return "Employee('{}', '{}', {}".format(self.first,self.last,self.pay)


