#!/usr/local/bin/python3.6


if __name__ == '__main__':
    for i in range(1, int(input())):
        print(sum(map(lambda x: i * 10 ** x, range(i))))
        # print(i, tuple(map(lambda x: i * 10 ** x, range(i))))
