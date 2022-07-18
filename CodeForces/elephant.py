# https://codeforces.com/problemset/problem/617/A
# A. Elephant

if __name__ == "__main__":
    x = int(input())
    step = 0
    while x > 0:
        if x >= 5:
            step += x // 5
            x %= 5
        elif x >= 4:
            step += x // 4
            x %= 4
        elif x >= 3:
            step += x // 3
            x %= 3
        elif x >= 2:
            step += x // 2
            x %= 2
        elif x >= 1:
            step += x // 1
            x %= 1
    print(step)
