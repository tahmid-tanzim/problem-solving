#!/usr/bin/python3
# https://www.hackerrank.com/challenges/drawing-book/problem


def replace_spaces(input_str, true_length):
    # i = true_length - 1
    # while i >= 0:
    #     if input_str[i] == ' ':
    #         input_str = input_str[:i] + '%20' + input_str[i + 1:]
    #     i -= 1

    i = 0
    while i < true_length:
        if input_str[i] == ' ':
            input_str = input_str[:i] + '%20' + input_str[i + 1:]
        i += 1

    return input_str


if __name__ == '__main__':
    print(replace_spaces("Mr John Smith      ", 13))

    # a = "Mr John Smith      "
    # i = 2
    # print(a[:i] + '%20' + a[i + 1:])



