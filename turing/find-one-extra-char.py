#!/usr/bin/python3


def find_one_extra_char(strA, strB):
    frequency = dict()
    for s1 in strA:
        if s1 in frequency:
            frequency[s1] += 1
        else:
            frequency[s1] = 1

    for s2 in strB:
        if s2 in frequency and frequency[s2] > 0:
            frequency[s2] -= 1
        else:
            return s2


if __name__ == "__main__":
    print(find_one_extra_char("abcd", "cbdea"))  # e
    print(find_one_extra_char("kxml", "klxml"))  # l
