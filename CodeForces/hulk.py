# https://codeforces.com/problemset/problem/705/A
# A. Hulk


if __name__ == "__main__":
    n = int(input())
    s = 'I hate '
    for i in range(1, n):
        s += 'that '
        if i % 2 != 0:
            s += 'I love '
        else:
            s += 'I hate '
    print(s + 'it')
