#!/usr/bin/python3
# https://leetcode.com/problems/two-sum/


# Time Complexity - O(n^2)
def twoNumberSum1(array, targetSum):
    i = 0
    while i < len(array) - 1:
        j = i + 1
        while j < len(array):
            if array[i] + array[j] == targetSum:
                return [array[j], array[i]]
            j += 1
        i += 1
    return []


# Store the Y in HashTable - O(n)
def twoNumberSum2(array, targetSum):
    HashTable = {}
    i = 0
    while i < len(array):
        x = array[i]
        if x in HashTable:
            return [x, targetSum - x]
        y = targetSum - x
        HashTable[y] = True
        i += 1
    return []


# Sort array O(nlog(n))
def twoNumberSum3(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
        else:
            return [array[left], array[right]]
    return []


if __name__ == '__main__':
    output1 = twoNumberSum1([3, 5, -4, 8, 11, 1, -1, 6], 10)
    # output2 = twoNumberSum2([3, 5, -4, 8, 11, 1, -1, 6], 10)
    # output3 = twoNumberSum3([3, 5, -4, 8, 11, 1, -1, 6], 10)

    print(f'{output1}')
    # print(f'{output2}')
    # print(f'{output3}')