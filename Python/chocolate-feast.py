#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://www.hackerrank.com/challenges/chocolate-feast/problem


def chocolate_feast(n, c, m):
    chocolates = n // c
    wrappers = chocolates

    while wrappers // m > 0:
        exchanged_chocolates = wrappers // m
        wrappers %= m
        wrappers += exchanged_chocolates
        chocolates += exchanged_chocolates

    return chocolates


if __name__ == '__main__':
    # print(chocolate_feast(15, 3, 2))  # 9
    # print(chocolate_feast(10, 2, 5))  # 6
    # print(chocolate_feast(12, 4, 4))  # 3
    print(chocolate_feast(6, 2, 2))  # 5
