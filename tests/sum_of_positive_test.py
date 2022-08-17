import unittest
from best_solution.sum_of_positive_best import positive_sum


class TestSumPositive(unittest.TestCase):

    def test_basic_test_cases(self):
        self.assertEquals(positive_sum([1, 2, 3, 4, 5]), 15)
        self.assertEquals(positive_sum([1, -2, 3, 4, 5]), 13)
        self.assertEquals(positive_sum([-1, 2, 3, 4, -5]), 9)

    def test_empty_case(self):
        self.assertEquals(positive_sum([]), 0)

    def test_negative_case(self):
        self.assertEquals(positive_sum([-1, -2, -3, -4, -5]), 0)


if __name__ == '__main__':
    unittest.main()
