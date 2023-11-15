# Name: Carlos Aguilera
# Class: CS30A -> 16195A
# SOURCE: https://en.wikipedia.org/wiki/Primality_test
from math import isqrt


# simple trial division test using sqrt
def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1

    # checks whether or not its even or odd
    if n % 2 == 0 or n % 3 == 0:
        return False

    # using integer sqrt so we dont use ceil
    end_point = isqrt(n)

    # checking for divisibility and if true return false
    for i in range(5, end_point + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


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


print(find_n_prime_fib(13))
