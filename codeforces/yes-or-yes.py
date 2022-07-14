# https://codeforces.com/problemset/problem/1703/A
# A. YES or YES?
if __name__ == "__main__":
    o = [input().lower() for _ in range(int(input()))]
    for i in o:
        print('YES' if i == 'yes' else 'NO')

