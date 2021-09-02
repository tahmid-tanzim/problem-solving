#!/usr/bin/python3

# if __name__ == '__main__':
#     N, M = [int(x) for x in input().split()]
#     i = N
#     A = []
#     while i > 0:
#         A.append(input().split())
#         i -= 1
#
#     for m in range(M):
#         for n in range(N):
#             print(A[n][m], end=' ')
#         print()


# def my_function():
#     """Do nothing, but document it.
#
#      No, really, it doesn't do anything.
#      """
#     i = 0
#     i += 1
#
#
# print(my_function.__doc__)


import time


def _allzip_(x, y):
    i = 0
    o = []
    for j in x:
        o.append((j, y[i]))
        i += 1
    return o


if __name__ == '__main__':
    a = list(range(1000))
    b = list(range(1000, 2000))

    start_time = time.time()
    ab_zip = zip(a, b)
    print(list(ab_zip))
    print("--- %s seconds ---" % (time.time() - start_time))

    # start_time = time.time()
    # ab_zip = _allzip_(a, b)
    # print(ab_zip)
    # print("--- %s seconds ---" % (time.time() - start_time))
