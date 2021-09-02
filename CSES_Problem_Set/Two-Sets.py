#!/usr/bin/python3
# https://cses.fi/problemset/task/1092

if __name__ == '__main__':
    n = int(input())
    _sum = int(n * (n+1) / 2)

    if _sum % 2 == 0:
        print('YES')
        _sum /= 2
        _set = [[], []]
        for i in range(n, 0, -1):
            if i <= _sum:
                _set[0].append(i)
                _sum -= i
            else:
                _set[1].append(i)
        print(len(_set[0]))
        print(*_set[0])
        print(len(_set[1]))
        print(*_set[1])
    else:
        print('NO')


