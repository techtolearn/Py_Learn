import unittest
from unittest.mock import patch
'''
we have to import as below else In PyCharm's Project tool window, right-click on the directory and select Mark Directory As -> Sources Root on imported module
to avoid red mark on import module or module not found 
#import sys  
'''

from Employee import Employee


class Testemplyee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass')
    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setup')
        self.emp1 = Employee('Tanvi','Satheesh',5000)
        self.emp2 = Employee('Divya','Satheesh',10000)

    def tearDown(self):
        print('tearDown\n')

    def test_email(self):
         print('test_email')
         self.assertEqual(self.emp1.email,'Tanvi.Satheesh@gmail.com')
         self.assertEqual(self.emp2.email,'Divya.Satheesh@gmail.com')
         self.emp1.first = 'Manasvi'
         self.emp2.last = 'Srirangapatna'
         self.assertEqual(self.emp1.email,'Manasvi.Satheesh@gmail.com')
         self.assertEqual(self.emp2.email,'Divya.Srirangapatna@gmail.com')

    def test_fulName(self):
        print('test_fulName')
        self.emp1 = Employee('Tanvi','Satheesh',5000)
        self.emp2 = Employee('Divya','Satheesh',10000)
        self.assertEqual(self.emp1.fulname,'Tanvi Satheesh')
        self.assertEqual(self.emp2.fulname,'Divya Satheesh')
        self.emp1.first = 'Manasvi'
        self.emp2.last = 'Srirangapatna'
        self.assertEqual(self.emp1.fulname,'Manasvi Satheesh')
        self.assertEqual(self.emp2.fulname,'Divya Srirangapatna')

    def test_apply_riase(self):
        print('test_apply_raise')
        self.emp1.pay = 6000
        self.emp2.pay = 11000
        self.assertEqual(self.emp1.apply_riase(),60000)
        self.assertEqual(self.emp2.apply_riase(),110000)

    def test_monthly_schedule(self):
        with patch('Employee.requests.get') as mocked_get:
            mocked_get.retun_value.ok = True
            mocked_get.retun_value.text = 'Success'

            schedule  = self.emp1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Satheesh/May')
            self.assertEqual(schedule, 'Success')

if __name__ == '__main__':
    unittest.main()


