#!/usr/local/bin/python3.6

if __name__ == '__main__':
    N, M = [int(x) for x in input().split()]
    i = N
    A = []
    while i > 0:
        A.append(input().split())
        i -= 1

    for m in range(M):
        for n in range(N):
            print(A[n][m], end=' ')
        print()
