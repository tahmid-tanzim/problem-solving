# https://codeforces.com/problemset/problem/996/A
# A. Hit the Lottery

if __name__ == "__main__":
    count = 0
    amount = int(input())
    while amount > 0:
        if amount >= 100:
            count += amount // 100
            amount = amount % 100
        elif amount >= 20:
            count += amount // 20
            amount = amount % 20
        elif amount >= 10:
            count += amount // 10
            amount = amount % 10
        elif amount >= 5:
            count += amount // 5
            amount = amount % 5
        elif amount >= 1:
            count += amount // 1
            amount = amount % 1
    print(count)

    
