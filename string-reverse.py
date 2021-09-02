#!/usr/bin/python3


def helper(index, text):
    if index >= len(text) or text is None:
        return

    helper(index + 1, text)
    print(text[index], end='')


if __name__ == '__main__':
    txt = "Tahmid Tanzim Lupin"
    helper(0, txt)

