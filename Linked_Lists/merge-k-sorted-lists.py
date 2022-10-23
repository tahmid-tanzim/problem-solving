#!/usr/bin/python3
# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def create(self, array: List[int]) -> Optional[ListNode]:
        n = len(array)
        if n == 0:
            return None

        root = ListNode(val=array[0])
        currentNode = root
        for i in range(1, n):
            currentNode.next = ListNode(val=array[i])
            currentNode = currentNode.next
        return root


def convertToLinkedList(array: List[List[int]]):
    ll = LinkedList()
    result = []
    for item in array:
        result.append(ll.create(item))
    return result


def convertToArray(node: Optional[ListNode]) -> List[int]:
    array = []
    while node is not None:
        array.append(node.val)
        node = node.next
    return array


class Solution1:
    # Brute force
    # Time Complexity - O(n * k^2)
    # n is size of lists
    # k is the largest size of one list
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)
        if n == 0:
            return None
        """
        [[1, 3, 3, 7], [4, 8, 9], [9, 10, 11]],
        """
        root = lists.pop()
        # while len(lists) > 0:
        #     pointerOne = root
        #     pointerTwo = lists.pop()
        #     while pointerOne is not None and pointerTwo is not None:
        #         if pointerOne.val < pointerTwo.val:
        #             node = pointerTwo
        #             pointerTwo = pointerTwo.next
        #             node.next = pointerOne.next
        #             pointerOne.next = node
        #         # elif pointerOne.val > pointerTwo.val:
        #         #     pass
        #         else:
        #             pass

        return root


if __name__ == '__main__':
    inputs = (
        # {
        #     "lists": [[1, 4, 5], [1, 3, 4], [2, 6]],
        #     "expected": [1, 1, 2, 3, 4, 4, 5, 6]
        # },
        {
            "lists": [],
            "expected": []
        },
        {
            "lists": [[]],
            "expected": []
        },
        # {
        #     "lists": [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]],
        #     "expected": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        # },
        {
            "lists": [[1, 3, 3, 7], [2, 4, 8, 9], [9, 10, 11]],
            "expected": [1, 2, 3, 3, 4, 7, 8, 9, 9, 10, 11]
        },
    )

    obj = Solution1()
    test_passed = 0
    for idx, val in enumerate(inputs):
        output = obj.mergeKLists(convertToLinkedList(val["lists"]))
        if convertToArray(output) == val['expected']:
            print(f"{idx}. CORRECT Answer\nOutput:   {output}\nExpected: {val['expected']}\n")
            test_passed += 1
        else:
            print(f"{idx}. WRONG Answer\nOutput:   {output}\nExpected: {val['expected']}\n")

    print(f"Passed: {test_passed:3}/{idx + 1}\n")
