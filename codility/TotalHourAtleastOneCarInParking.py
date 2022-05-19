#!/usr/bin/python3


if __name__ == "__main__":
    n = int(input())
    time = [False] * 24
    for i in range(n):
        start, end = [int(j) for j in input().split()]
        time[start:end] = [True] * (end-start)

    print(time.count(True))
    # print(sum(1 for t in time if t is True))
