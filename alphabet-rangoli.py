#!/usr/local/bin/python3.6

import string


def print_rangoli(size):
    width = 4 * size - 3
    alphabet = string.ascii_lowercase
    lines = []
    i = size - 1
    while i >= 0:
        right = alphabet[i:size]
        left = right[::-1][:-1]
        full_txt = '-'.join(list(left + right)).center(width, '-')
        if i != 0:
            lines.insert(0, full_txt)
        print(full_txt)
        i -= 1

    for line in lines:
        print(line)


def main():
    for i in (1, 3, 5, 10):
        print_rangoli(i)


if __name__ == '__main__':
    main()


# 3 -> 9
# 5 -> 17
# 10 -> 37