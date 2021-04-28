#!/usr/bin/python3
# Cracking the Coding Interview - 8.1


# Dynamic Programming
def tripleStep(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    return tripleStep(n - 1) + tripleStep(n - 2) + tripleStep(n - 3)


if __name__ == "__main__":
    print(f'Answer - {tripleStep(5)}')
