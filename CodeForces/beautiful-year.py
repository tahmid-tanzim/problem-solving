# https://codeforces.com/problemset/problem/271/A
# A. Beautiful Year

def isDistinctDigits(year):
    frequency = {}
    for i in range(1, 5):
        digit = (year % (10 ** i) - year % (10 ** (i - 1))) // (10 ** (i - 1))
        if digit in frequency:
            return False
        frequency[digit] = 1
    return True


if __name__ == "__main__":
    y = int(input()) + 1
    while not isDistinctDigits(y):
        y += 1
    print(y)


