#!/usr/bin/python3


def sort_words(string):
    output = string.split(' ')
    output.sort(key=lambda e: e.lower())
    return output


if __name__ == "__main__":
    print(sort_words('banana ORANGE apple'))
