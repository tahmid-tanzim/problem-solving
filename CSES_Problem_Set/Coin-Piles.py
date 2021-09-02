#!/usr/bin/python3
# https://cses.fi/problemset/task/1754


def xnor(a, b):
    return (a == 0 and b == 0) or (a != 0 and b != 0)


if __name__ == '__main__':
    n = int(input())
    output = []
    while n > 0:
        coins = list(map(int, input().split()))
        output.append("YES" if sum(coins) % 3 == 0 and xnor(*coins) else "NO")
        n -= 1
    print(*output, sep='\n')
