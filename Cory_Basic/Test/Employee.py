'''
https://www.youtube.com/watch?v=pd-0G0MigUA&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=51
Python SQLite Tutorial: Complete Overview - Creating a Database, Table, and Running Queries
'''
import requests

class Employee:
    amount =10
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

    def apply_riase(self):
        return self.pay*self.amount

    def monthly_schedule(self,month):
        return requests.get(f'http://company.com/{self.last}/{self.month}')
        if reponse.ok:
            return reponse.text
        else:
            return 'Bad Response'

