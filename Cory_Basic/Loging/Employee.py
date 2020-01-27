'''
https://www.youtube.com/watch?v=-ARI4Cz-awo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=52
'''
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler =  logging.FileHandler('employe.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class Employee:
    def __init__(self,first,last):
        self.first = first
        self.last = last

        logger.info('Created Employee: {} - {}'.format(self.fulname, self.email))

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first,self.last)

    @property
    def fulname(self):
        return '{} {}'.format(self.first,self.last)


emp_1 = Employee('Tanvi','Satheesh')
emp_2 = Employee('Divya','Srirangapatna Jaikumar')
emp_3 = Employee('Satheesh','Kumar')
