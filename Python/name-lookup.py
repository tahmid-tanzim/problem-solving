#!/usr/local/bin/python3.6

if __name__ == '__main__':
    N = int(input())
    names = []
    while N > 0:
        i, name = input().split()
        names.insert(int(i) - 1, name)
        N -= 1

    N = int(input())
    while N > 0:
        i = int(input())
        print(names[i - 1])
        N -= 1

