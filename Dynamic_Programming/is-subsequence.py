#!/usr/bin/python3
# https://leetcode.com/problems/is-subsequence/


def isSubsequence(s: str, t: str, i: int, j: int) -> bool:
    if i == 0:
        return True
    if j == 0:
        return False

    if s[i - 1] == t[j - 1]:
        return isSubsequence(s, t, i - 1, j - 1)

    return isSubsequence(s, t, i, j - 1)


if __name__ == "__main__":
    testcase = (
        {
            "s": "abc",
            "t": "ahbgdc",
            "output": True
        },
        {
            "s": "axc",
            "t": "ahbgdc",
            "output": False
        },
        {
            "s": "AXY",
            "t": "ADXCPY",
            "output": True
        },
        {
            "s": "AXY",
            "t": "YADXCP",
            "output": False
        },
        {
            "s": "gksrek",
            "t": "geeksforgeeks",
            "output": True
        },
    )

    for test in testcase:
        print(isSubsequence(test["s"], test["t"], len(test["s"]), len(test["t"])))
