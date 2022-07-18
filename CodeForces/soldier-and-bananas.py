# https://codeforces.com/problemset/problem/546/A
# A. Soldier and Bananas

if __name__ == "__main__":
    k, n, w = map(int, input().split())
    total_amount = 0
    for i in range(1, w + 1):
        total_amount += k * i
    print(total_amount - n if total_amount > n else 0)
