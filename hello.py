#!/usr/bin/python3


def isGood():
    print('isGood')
    return True


def isBad():
    print('isBad')
    return False


if __name__ == '__main__':
    if isBad() and isGood():
        print("Hello")
    else:
        print("World")
