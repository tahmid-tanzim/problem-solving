#!/usr/bin/python3

cube = lambda x: x ** 3


def fibonacci(n):
    l = []
    for i in range(n):
        l.append(i if i <= 1 else l[i-1] + l[i-2])
    return l


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    # print(fibonacci(n))

