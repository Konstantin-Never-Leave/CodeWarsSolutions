import unittest
from best_solution.fun_numbers_best import dig_pow


class TestFunNumbers(unittest.TestCase):

    def test_fun_numbers(self):
        self.assertEquals(dig_pow(89, 1), 1)
        self.assertEquals(dig_pow(92, 1), -1)
        self.assertEquals(dig_pow(46288, 3), 51)


if __name__ == '__main__':
    unittest.main()
