# https://codeforces.com/problemset/problem/231/A
# A. Team


if __name__ == "__main__":
    count = 0
    for _ in range(int(input())):
        total = sum(map(int, input().split()))
        if total > 1:
            count += 1
    print(count)

