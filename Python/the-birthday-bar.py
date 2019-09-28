#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://www.hackerrank.com/challenges/the-birthday-bar/problem


def birthday(s, d, m):
    n, count = len(s), 0
    for i in range(n - m + 1):
        if sum(s[i:i + m]) == d:
            count += 1
    return count


if __name__ == '__main__':
    print(birthday([1, 2, 1, 3, 2], 3, 2))  # 2
    # print(birthday([1, 1, 1, 1, 1, 1], 3, 2))  # 0
    # print(birthday([4], 4, 1))  # 1
    # print(birthday([2, 2, 1, 3, 2], 4, 2))  # 2
