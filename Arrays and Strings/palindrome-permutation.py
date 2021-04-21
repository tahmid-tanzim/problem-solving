#!/usr/bin/python3
# Cracking the Coding Interview - 1.4
from typing import List


class PermutationOfPalindrome:
    def __init__(self):
        pass

    def getCharNumber(self, char: str) -> int:
        a = ord('a')
        z = ord('z')
        A = ord('A')
        Z = ord('Z')
        val = ord(char)
        if A <= val <= Z:
            return val - A
        if a <= val <= z:
            return val - a
        return -1

    def buildCharFrequencyTable(self, phrase: str) -> List[int]:
        table = [0] * 26
        for c in phrase:
            x = self.getCharNumber(c)
            if x != -1:
                table[x] += 1
        return table

    def checkMaxOneOdd(self, table):
        foundOdd = False
        for count in table:
            if count % 2 == 1:
                if foundOdd:
                    return False
                foundOdd = True
        return True

    def solutionOne(self, phrase: str):
        """
        Time - O(n)
        """
        table = self.buildCharFrequencyTable(phrase)
        return self.checkMaxOneOdd(table)

    def solutionTwo(self, phrase: str):
        """
        Time - O(n)
        """
        countOdd = 0
        table = [0] * 26
        for c in phrase:
            x = self.getCharNumber(c)
            if x == -1:
                continue
            table[x] += 1
            if table[x] % 2 == 1:
                countOdd += 1
            else:
                countOdd -= 1
        return countOdd <= 1


if __name__ == '__main__':
    o = PermutationOfPalindrome()
    print(f'{o.solutionOne("Tact Coa")}')
    print(f'{o.solutionTwo("Tact Coa")}')
