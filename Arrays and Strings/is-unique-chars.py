#!/usr/bin/python3
# Cracking the Coding Interview - 1.1

def isUniqueChars(s):
    checker = 0
    n = len(s)
    for i in range(n):
        val = ord(s[i]) - ord('a')
        if (checker & (1 << val)) > 0:
            print(i, s[i])
            return False
        checker |= (1 << val)
    return True


if __name__ == '__main__':
    output1 = isUniqueChars("asdertysg")
    print(f'{output1}')

    # for i in range(1, 11):
    #     print(i, i << i)
