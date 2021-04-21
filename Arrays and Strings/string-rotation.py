#!/usr/bin/python3
# Cracking the Coding Interview - 1.9


def isSubstring(string: str, sub: str):
    string_length = len(string)
    j = 0
    while j < string_length and string[j] != sub[0]:
        j += 1

    if j >= string_length:
        return False

    for i in range(len(sub)):
        if string[j] != sub[i]:
            return False
        j += 1

    return True


def isRotation(s1: str, s2: str):
    """
    s1 = xy = waterbottle
    s2 = yx = erbottlewat
    x = wat
    y = erbottle

    if s2[yx] is substring of s1s1[xyxy] then True else False
    """
    n1 = len(s1)
    if n1 == len(s2) and n1 > 0:
        return isSubstring(s1 + s1, s2)
    return False


if __name__ == '__main__':
    output = isRotation(s1="waterbottle", s2="erbottlewat")
    # output = isRotation(s1="zrtyuioplkj", s2="erbotylewat")
    print(f'{output}')
