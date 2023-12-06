#!/usr/bin/python3
# https://leetcode.com/problems/decode-string/
from typing import List


def decodeString(s: str) -> str:
    # i = 0
    # n = len(s)
    # numberStack: []
    # numberStr = ""
    # subStrStack: []
    # subStr = ""
    # while i < n:
    #     code = ord(s[i])
    #     if 48 <= code <= 57:
    #         numberStr += s[i]
    #     elif code == 91:
    #         numberStack.append(int(numberStr))
    #         numberStr = ""
    #     elif 97 <= code <= 122:
    #         subStr += s[i]
    #     elif code == 93:
    #         numberStack.append(int(numberStr))
    #         numberStr = ""
    #     i += 1
    pass


if __name__ == "__main__":
    testcase = (
        {
            "s": "3[a]2[bc]",
            "output": "aaabcbc"
        },
        {
            "s": "3[a2[c]]",
            "output": "accaccacc"
        },
        {
            "s": "2[abc]3[cd]ef",
            "output": "abcabccdcdcdef"
        },
    )

    for test in testcase:
        result = decodeString(test["s"], [])
        print(result, result == test["output"])


# "3[a2[c]]", 0, [], []
#
# "3[a2[c]]", 1, [3], []
#
# "3[a2[c]]", 2, [3], [a]
#
# "3[a2[c]]", 3, [3], [a]
#
# "3[a2[c]]", 4, [3, 2], [a]
#
# "3[a2[c]]", 5, [3, 2], [a, c]
#
# "3[a2[c]]", 6, [3, 2], [a, c] = cc
# "3[a2[c]]", 7, [3], [] = acc
#
# accaccacc

# "2[2abc]3[cd]ef", 0, [], []
# "2[abc]3[cd]ef", 5, [2], ['abc'] = 'abcabc'
# "2[abc]3[cd]ef", 6, [3], [cd] = 'abcabc'