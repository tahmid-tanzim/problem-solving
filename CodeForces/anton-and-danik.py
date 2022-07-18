# https://codeforces.com/problemset/problem/734/A
# A. Anton and Danik

if __name__ == "__main__":
    n = int(input())
    string = input()
    won = {'A': 0, 'D': 0}

    for char in string:
        won[char] += 1

    if won['A'] > won['D']:
        print('Anton')
    elif won['A'] < won['D']:
        print('Danik')
    else:
        print('Friendship')
