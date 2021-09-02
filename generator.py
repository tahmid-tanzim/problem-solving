#!/usr/bin/python3


def is_prime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
        else:
            return True


def primes(n, last):
    while n < last:
        if is_prime(n):
            yield n
        n += 1


for n in primes(1, 70):
    # if n > 100:
    #     break
    print(n)
