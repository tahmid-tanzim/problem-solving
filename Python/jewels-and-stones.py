# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for j in J:
            for s in S:
                if j == s:
                    count = count + 1
        return count


o = Solution()
print(o.numJewelsInStones("aA", "aAAbbbb")) # 3
print(o.numJewelsInStones("z", "ZZ")) # 0
