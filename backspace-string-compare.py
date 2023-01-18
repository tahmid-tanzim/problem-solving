#!/usr/bin/python3
# https://leetcode.com/problems/backspace-string-compare/


def trimString(string: str) -> str:
    n = len(string)
    i = 0
    while i < n:
        char = string[i]
        if char == "#":
            if i > 0:
                string = string[:i - 1] + string[i + 1:]
                i -= 1
                n -= 2
            else:
                string = string[i + 1:]
                n -= 1
        else:
            i += 1
    print(string)
    return string


def backspaceCompare(s: str, t: str) -> bool:
    return trimString(s) == trimString(t)


if __name__ == "__main__":
    testcase = (
        {
            "s": "#ab#c",
            "t": "ad#c",
            "output": True
        },
        {
            "s": "ab##",
            "t": "c#d#",
            "output": True
        },
        {
            "s": "a#c",
            "t": "b",
            "output": False
        },
    )

    for test in testcase:
        result = backspaceCompare(test["s"], test["t"])
        print(result, result == test["output"])
