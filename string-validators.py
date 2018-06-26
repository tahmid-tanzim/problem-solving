#!/usr/local/bin/python3.6


if __name__ == '__main__':
    s = input()
    for validation_method in ('isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'):
        print(any(list(map(lambda x: eval("x." + validation_method + "()"), s))))
