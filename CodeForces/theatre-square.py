# https://codeforces.com/problemset/problem/1/A
# A. Theatre Square
from math import ceil


if __name__ == "__main__":
    n, m, a = map(int, input().split())
    print(ceil(n/a) * ceil(m/a))
