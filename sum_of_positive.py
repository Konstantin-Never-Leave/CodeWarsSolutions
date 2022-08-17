# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]
""" Playing with digits

Some numbers have funny properties. For example:

89 --> 8¹ + 9² = 89 * 1

695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2

46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51

Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive
powers of p is equal to k * n.
In other words:

Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k

If it is the case we will return k, if not return -1.

Note: n and p will always be given as strictly positive integers.
"""

# -------------------------------------------------->mine solution:<----------------------------------------------------

def positive_sum(mixed_array):
    positive_sum = []
    for i in mixed_array:
        if i > 0:
            positive_sum.append(i)
    return sum(positive_sum) if positive_sum else 0

# -------------------------------------------------->best solution:<----------------------------------------------------

def positive_sum(arr):
    return sum(filter(lambda x: x > 0,arr))

# ______________________________________________________TESTS___________________________________________________________

import codewars_test as test
from solution import positive_sum

@test.describe("positive_sum")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(positive_sum([1,2,3,4,5]),15)
        test.assert_equals(positive_sum([1,-2,3,4,5]),13)
        test.assert_equals(positive_sum([-1,2,3,4,-5]),9)

    @test.it("returns 0 when array is empty")
    def empty_case():
        test.assert_equals(positive_sum([]),0)

    @test.it("returns 0 when all elements are negative")
    def negative_case():
        test.assert_equals(positive_sum([-1,-2,-3,-4,-5]),0)

# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]