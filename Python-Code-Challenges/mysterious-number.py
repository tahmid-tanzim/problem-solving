#!/usr/bin/python3


def isPalindrome(x: int) -> bool:
    string = str(x)
    n = len(string)
    startIdx = 0
    while startIdx < n//2:
        endIdx = n - startIdx - 1
        if string[startIdx] != string[endIdx]:
            return False
        startIdx += 1
    return True


def reverse(x: int) -> int:
    n = str(x)
    return int(n[::-1])


def findPalindromeInTotal(originalNumber, reverseNumber, hashTable, checkLimit):
    oNum = originalNumber
    rNum = reverseNumber
    while checkLimit > 0:
        total = oNum + rNum
        # print(f"{oNum} + {rNum} = {total}")
        if isPalindrome(total):
            return
        else:
            oNum = total
            rNum = reverse(oNum)
        checkLimit -= 1
    hashTable.append(originalNumber)


def findMysteriousNumber():
    hashTable = list()
    for originalNumber in range(101, 1000):
        reverseNumber = reverse(originalNumber)
        findPalindromeInTotal(originalNumber, reverseNumber, hashTable, 10)
    return hashTable


if __name__ == "__main__":
    output = findMysteriousNumber()
    print(output)
    print(len(output))
