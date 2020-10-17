import math
from typing import List

class Solution:
    def prevSum(self, i: int, j: int) -> int:
        if j == 1 or i == j:
            return 1
        else:
            first = self.prevSum(i - 1, j - 1)
            second = self.prevSum(i - 1, j)
            return first + second

    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex <= 0:
            return [1]

        output = []
        mid = math.ceil((rowIndex + 1) / 2)
        for x in range(mid):
            output.append(self.prevSum(rowIndex + 1, x + 1))
        return output + (output[::-1] if mid % 2 == 0 else output[1::-1])
