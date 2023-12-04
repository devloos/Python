# Name: Carlos Aguilera
# Class: CS30A -> 16195A
# SOURCE: https://en.wikipedia.org/wiki/Primality_test
import random
from math import isqrt
from sympy import isprime

# Utility function to do
# modular exponentiation.
# It returns (x^y) % p


def modular_exponentiation(x, y, p):

    # Initialize result
    res = 1

    # Update x if it is more than or
    # equal to p
    x = x % p
    while (y > 0):

        # If y is odd, multiply
        # x with result
        if (y & 1):
            res = (res * x) % p

        # y must be even now
        y = y >> 1  # y = y/2
        x = (x * x) % p

    return res

# This function is called
# for all k trials. It returns
# false if n is composite and
# returns false if n is
# probably prime. d is an odd
# number such that d*2<sup>r</sup> = n-1
# for some r >= 1


def rabin_test(d, n):

    # Pick a random number in [2..n-2]
    # Corner cases make sure that n > 4
    a = 2 + random.randint(1, n - 4)

    # Compute a^d % n
    x = modular_exponentiation(a, d, n)

    if (x == 1 or x == n - 1):
        return True

    # Keep squaring x while one
    # of the following doesn't
    # happen
    # (i) d does not reach n-1
    # (ii) (x^2) % n is not 1
    # (iii) (x^2) % n is not n-1
    while (d != n - 1):
        x = (x * x) % n
        d *= 2

        if (x == 1):
            return False
        if (x == n - 1):
            return True

    # Return composite
    return False

# It returns false if n is
# composite and returns true if n
# is probably prime. k is an
# input parameter that determines
# accuracy level. Higher value of
# k indicates more accuracy.


def is_prime(n):

    # Corner cases
    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True

    # Find r such that n =
    # 2^d * r + 1 for some r >= 1
    d = n - 1
    while (d % 2 == 0):
        d //= 2

    return rabin_test(d, n)


# use hashmap for memo because why not
fib_dict = {}


def fib(a: int) -> int:
    if (a <= 1):
        return a

    # if in dict then use previous fib calculation
    if (fib_dict.get(a) != None):
        return fib_dict[a]

    fib_dict[a] = fib(a - 1) + fib(a - 2)
    return fib_dict[a]


def find_n_prime_fib(num: int) -> list:
    if (num < 0):
        raise Exception()

    i = 0
    prime_list = []

    # we check all number increasing i by one and stop once we fill our prime list
    while (len(prime_list) < num):
        fib_result = fib(i)

        if (is_prime(fib_result)):
            prime_list.append(fib_result)

        i += 1

    return prime_list


print(find_n_prime_fib(20))
