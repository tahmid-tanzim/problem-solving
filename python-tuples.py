#!/usr/local/bin/python3.6


def main():
    n = int(input())
    t = tuple(map(int, input().split()))
    print(hash(t))


if __name__ == '__main__':
    main()