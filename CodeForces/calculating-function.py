# https://codeforces.com/problemset/problem/486/A
# A. Calculating Function

if __name__ == "__main__":
    n = int(input())
    result = 0
    if n % 2 == 0:
        result = n // 2
    else:
        result = (n - 1) // 2 - n
    print(result)
