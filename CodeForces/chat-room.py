# https://codeforces.com/problemset/problem/58/A
# A. Chat Room

if __name__ == "__main__":
    i = 0
    target = 'hello'
    for char in input():
        if i >= 5:
            break
        elif char == target[i]:
            i += 1
    print('YES' if i == 5 else 'NO')