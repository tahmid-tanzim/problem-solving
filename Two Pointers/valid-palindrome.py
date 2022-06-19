#!/usr/bin/python3
# https://leetcode.com/problems/valid-palindrome/


def isPalindrome(s: str) -> bool:
    """
    Time  - O(n)
    Space - O(n)
    """
    newStr = str()
    for c in s:
        if c.isalnum():
            newStr += c.lower()
    return newStr == newStr[::-1]


def isAlphaNumeric(c: str) -> bool:
    return (97 <= ord(c) <= 122) or (65 <= ord(c) <= 90) or (48 <= ord(c) <= 57)


def isPalindrome2(s: str) -> bool:
    """
    Time  - O(n)
    Space - O(1)
    """
    leftPointer = 0
    rightPointer = len(s) - 1
    while leftPointer < rightPointer:
        while leftPointer < rightPointer and not isAlphaNumeric(s[leftPointer]):
            leftPointer += 1

        while leftPointer < rightPointer and not isAlphaNumeric(s[rightPointer]):
            rightPointer -= 1

        if s[leftPointer].lower() != s[rightPointer].lower():
            return False

        leftPointer += 1
        rightPointer -= 1
    return True


if __name__ == '__main__':
    inputs = (
        {
            "s": "A man, a plan, a canal: Panama",
            "expected": True
        },
        {
            "s": "race a car",
            "expected": False
        },
        {
            "s": " ",
            "expected": True
        },
    )

    test_passed = 0
    for idx, val in enumerate(inputs):
        output = isPalindrome2(val["s"])
        if output == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:   {output}\nExpected: {val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
