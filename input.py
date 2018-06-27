#!/usr/local/bin/python3.6


if __name__ == '__main__':
    (x, k) = tuple(map(int, input().split()))
    P = input().replace("x", str(x))
    print(eval(P) == k)
