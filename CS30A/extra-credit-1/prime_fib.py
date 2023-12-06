# Name: Carlos Aguilera
# Class: CS30A -> 16195A
# SOURCE: https://en.wikipedia.org/wiki/Primality_test
import random


# I tried implementing my own miller rabin but it did not work

# def find_m(n: int) -> int:
#     m = 0
#     i = 1
#     while (True):
#         num = n / (2 ** i)
#         if (not num.is_integer()):
#             break

#         i += 1
#         m = num

#     return m


# def is_prime(n):

#     # Corner cases
#     if (n <= 1 or n == 4):
#         return False
#     if (n <= 3):
#         return True

#     m = find_m(n - 1)
#     a = random.randint(1, n - 1)

#     bi = (a ** m) % n

#     if (bi == 1 or bi == -1):
#         return False

#     while (True):
#         bi = (bi ** 2) % n

#         if (bi == 1):
#             return True
#         elif (bi == -1):
#             return False


def is_prime(n):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n != int(n):
        return False
    n = int(n)
    # Miller-Rabin test for prime
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        return False

    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    s = 0
    d = n-1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert (2**s * d == n-1)

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True

    for i in range(8):  # number of trials
        a = random.randrange(2, n)
        if trial_composite(a):
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


def main():
    print(find_n_prime_fib(20))


if __name__ == "__main__":
    main()
