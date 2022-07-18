# https://codeforces.com/problemset/problem/791/A
# A. Bear and Big Brother


if __name__ == "__main__":
    a, b = map(int, input().split())
    year = 0
    while a <= b:
        a *= 3
        b *= 2
        year += 1
    print(year)
