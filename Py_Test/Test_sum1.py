import unittest

class Test_sum1(unittest.TestCase):

    def Test_sum1(self):
        self.assertEqual(sum((1,2,3)),6,'should be 6')

    def Test_sumtupl(self):
        self.assertEqual(sum([1,2,2]),5,'should be 5')

if __name__ == '__main__':
        unittest.main()
        print("Everything passed")


