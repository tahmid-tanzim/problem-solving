def sieve(limit):
    """Generates a list of prime numbers up to a given limit using the Sieve of Atkin."""
    if limit < 2:
        return []

    # Create sieve list initialized to False
    res = [False] * (limit + 1)

    if limit >= 2:
        res[2] = True
    if limit >= 3:
        res[3] = True

    x = 1
    while x * x <= limit:
        y = 1
        while y * y <= limit:
            # 4x2+y2=n is odd and modulo-12 remainder is 1 or 5
            n = (4 * x * x) + (y * y)
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                res[n] ^= True

            # 3x2+y2=n is odd and modulo-6 remainder is 1
            n = (3 * x * x) + (y * y)
            if n <= limit and n % 12 == 7:
                res[n] ^= True

            # 3x2-y2=n is odd and modulo-12 remainder is 11
            n = (3 * x * x) - (y * y)
            if x > y and n <= limit and n % 12 == 11:
                res[n] ^= True
            y += 1
        x += 1

    # Checking for square free condition
    r = 5
    while r * r <= limit:
        if res[r]:
            for multiple in range(r * r, limit + 1, r * r):
                # print(f'For index:{r} multiple:{multiple}')
                res[multiple] = False
        r += 1

    # Collect prime numbers into a list
    prime_number_list = []
    for i in range(len(res)):
        is_prime = res[i]
        if is_prime:
            prime_number_list.append(i)
    return prime_number_list


def pick_prime(primes, min_size=1000):
    """Returns a suitable prime to use as modulus."""
    for prime in primes:
        if prime >= min_size:
            return prime

    return primes[-1] if primes else None  # Return last prime if none are large enough


def hash(string, modulus):
    """Implements polynomial rolling hash of string keys."""
    hash_value = 5381
    p = 33
    p_pow = 1
    # print("String:", string)
    for char in string:
        hash_value = (hash_value + (ord(char) - ord('a') + 1) * p_pow) % modulus
        # print("Char:", char, "Hash Value:", hash_value)
        p_pow = (p_pow * p) % modulus
    return hash_value


if __name__ == '__main__':
    # Generate primes list to use as modulus
    primes = sieve(10000)  # Modify limit based on needs
    # primes = sieve(100)  # Modify limit based on needs
    # print(primes)
    modulus = pick_prime(primes, 1000)

    if modulus is None:
        print("Sorry! No suitable prime found.")
    else:
        test_array = ["alpha", "beta", "gamma", "delta", "epsilon"]
        for string in test_array:
            hash_value = hash(string, modulus)
            print(f"Hash of '{string}' is {hash_value}")
