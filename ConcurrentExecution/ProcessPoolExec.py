import concurrent.futures
import math
from time import perf_counter

PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def main():
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))


# def main():
#     for number in PRIMES:
#         print('%d is prime: %s' % (number, is_prime(number)))


if __name__ == '__main__':
    start_time = perf_counter()
    main()
    print(f'Function took {(perf_counter() - start_time):.4f} seconds')
