import unittest
from best_solution.century_from_year_best import century


class TestSumPositive(unittest.TestCase):

    def test_basic_cases(self):
        self.assertEquals(century(1705), 18, 'Testing for year 1705')
        self.assertEquals(century(1900), 19, 'Testing for year 1900')
        self.assertEquals(century(1601), 17, 'Testing for year 1601')
        self.assertEquals(century(2000), 20, 'Testing for year 2000')
        self.assertEquals(century(356), 4, 'Testing for year 356')
        self.assertEquals(century(89), 1, 'Testing for year 89')


if __name__ == '__main__':
    unittest.main()
