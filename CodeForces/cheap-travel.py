# https://codeforces.com/problemset/problem/466/A
# A. Cheap Travel

if __name__ == "__main__":
    n, m, a, b = map(int, input().split())
    money_required = 0
    if b / m <= a:
        money_required = (n // m) * b
        n %= m
        money_required += min(n * a, b)
    else:
        money_required = n * a
    print(money_required)
