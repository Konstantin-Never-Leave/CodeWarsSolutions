import collections
import itertools
import tests.fun_numbers_test as tr


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
