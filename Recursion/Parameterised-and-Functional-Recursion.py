#!/usr/bin/python3


# Parameterised Recursion
def calculateSum1(i, total):
    if i == 0:
        return total

    return calculateSum1(i - 1, total + i)


# Functional Recursion
def calculateSum2(i):
    if i == 0:
        return 0

    return i + calculateSum2(i - 1)


if __name__ == "__main__":
    print(calculateSum1(10, 0))
    print(calculateSum2(10))
