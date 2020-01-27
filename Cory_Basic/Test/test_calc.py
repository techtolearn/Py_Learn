import  unittest

import calc


class TestCalc(unittest.Testcase):

    def test_add(self):
        #result = calc.add(10.5)
        self.assertEqual(calc.add(10.5),15)

    if __name__ == '__main__':
        unittest.main()

