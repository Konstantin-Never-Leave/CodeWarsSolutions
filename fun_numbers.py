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

import collections
import itertools


def get_prime_divisors(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            n /= i
            yield i
        else:
            i += 1
    if n > 1:
        yield n


def calc_product(iterable):
    acc = 1
    for i in iterable:
        acc *= i

    return acc


def get_all_divisors(dividend):
    primes = get_prime_divisors(dividend)
    primes_counted = collections.Counter(primes)
    divisors_exponentiated = [[div ** i for i in range(count + 1)] for div, count in primes_counted.items()]
    for prime_exp_combination in itertools.product(*divisors_exponentiated):
        yield calc_product(prime_exp_combination)


def dig_pow(n, p):
    the_sum = int()
    for i in str(n):
        g = int(i)**p
        the_sum += g
        p += 1
    if max(list(get_all_divisors(the_sum))) % n == 0:
        final_result = max(list(get_all_divisors(the_sum))) / n
    else:
        final_result = -1

    return final_result

# -------------------------------------------------->best solution:<----------------------------------------------------

def dig_pow(number, power):
    the_sum = int()
    for index, value in enumerate(str(number)):
        the_sum += pow(int(value), power + index)
    return the_sum / number if the_sum % number == 0 else -1

# ______________________________________________________TESTS___________________________________________________________

test.assert_equals(dig_pow(89, 1), 1)
test.assert_equals(dig_pow(92, 1), -1)
test.assert_equals(dig_pow(46288, 3), 51)

# [][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][][]