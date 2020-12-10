#!/usr/local/bin/python3


def get_prime_factors(n):
    divisor = 2
    prime_factors = []
    while divisor <= n:
        if n % divisor == 0:
            prime_factors.append(divisor)
            n = n // divisor
        else:
            divisor += 1
    return prime_factors


if __name__ == "__main__":
    print(get_prime_factors(630))
