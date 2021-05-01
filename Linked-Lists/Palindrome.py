#!/usr/bin/python3
"""
LinkedList - 2.6. Palindrome
"""
from typing import List
from LinkedList import Node


class ReverseAndCompare:
    """
    Solution 1
    O(n) time
    O(n) space
    """
    def __init__(self, h=None):
        self.head = h

    def _reverseAndClone(self) -> Node:
        current_node = self.head
        reversed_head: Node = None
        while current_node is not None:
            node: Node = Node(current_node.data)
            node.next = reversed_head
            reversed_head = node
            current_node = current_node.next
        return reversed_head

    def isPalindrome(self) -> bool:
        current_node = self.head
        reversed_node: Node = self._reverseAndClone()
        while current_node is not None and reversed_node is not None:
            if current_node.data != reversed_node.data:
                return False
            current_node = current_node.next
            reversed_node = reversed_node.next

        return current_node is None and reversed_node is None


class IterativeApproach:
    """
    Solution 2 using stack
    O(n) time
    O(n) space
    """
    def __init__(self, h=None):
        self.head = h

    def isPalindrome(self) -> bool:
        fast = slow = self.head
        stack: List[int] = list()
        while fast is not None and fast.next is not None:
            stack.append(slow.data)
            slow = slow.next
            fast = fast.next.next

        # By pass middle node of odd length linkedList
        if fast is not None:
            slow = slow.next

        while slow is not None:
            val = stack.pop()
            if slow.data != val:
                return False
            slow = slow.next

        return True


if __name__ == "__main__":
    TEST_CASES = [
        {
            "id": 1,
            "input": [1, 2, 3, 4, 3, 2, 1],
            "output": True
        },
        {
            "id": 2,
            "input": [1, 2, 3, 4, 4, 3, 2, 1],
            "output": True
        },
        {
            "id": 3,
            "input": [1, 2, 3, 4, 5, 3, 2, 1],
            "output": False
        },
        {
            "id": 5,
            "input": [1, 2, 3, 4, 2, 1, 1],
            "output": False
        }
    ]

    for testCase in TEST_CASES:
        head = tail = None
        for i in testCase["input"]:
            new_node = Node(i)
            if head is None:
                head = tail = new_node
            else:
                tail.next = new_node
                tail = new_node

        objects = (
            ReverseAndCompare(head),
            IterativeApproach(head),
        )

        for obj in objects:
            output = obj.isPalindrome()

            if output == testCase["output"]:
                print(f'TEST #{testCase["id"]} PASSED | {obj.__class__.__name__}')
            else:
                print(f'TEST #{testCase["id"]} FAILED | {obj.__class__.__name__}')
