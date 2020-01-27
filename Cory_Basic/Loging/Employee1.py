'''
https://www.youtube.com/watch?v=-ARI4Cz-awo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=52
'''
import logging


logging.basicConfig(filename='employe1.log', level=logging.INFO,
     format='%(asctime)s:%(levelname)s:%(message)s')

class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last

        logging.info('Created Employee: {} - {}'.format(self.fulname, self.email))

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)

    @property
    def fulname(self):
        return '{} {}'.format(self.first,self.last)


emp_1 = Employee('Tanvi','Satheesh')
emp_2 = Employee('Divya','Srirangapatna Jaikumar')
emp_3 = Employee('Satheesh','Kumar')
