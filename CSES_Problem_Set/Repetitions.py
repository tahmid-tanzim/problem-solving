#!/usr/local/bin/python3
# https://cses.fi/problemset/task/1069

if __name__ == '__main__':
    output = count = 0
    char = ''
    string = input()
    for s in string:
        if char == s:
            count += 1
        else:
            output = max(count, output)
            char, count = s, 1
    print(max(count, output))
