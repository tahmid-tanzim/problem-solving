# https://codeforces.com/problemset/problem/4/A
# A. Watermelon
if __name__ == "__main__":
    w = int(input())
    if 1 <= w <= 3 or w % 2 == 1:
        print('NO')
    else:
        print('YES')
