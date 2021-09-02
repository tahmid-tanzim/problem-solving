#!/usr/bin/python3


def main():
    (N, M) = map(int, input().split())
    center = N // 2

    for i in range(center):
        print((".|." * (2 * i + 1)).center(M, '-'))

    print('WELCOME'.center(M, '-'))

    for i in reversed(range(center)):
        print((".|." * (2 * i + 1)).center(M, '-'))


if __name__ == '__main__':
    main()