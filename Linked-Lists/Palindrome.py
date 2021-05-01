#!/usr/bin/python3
"""
LinkedList - 2.6. Palindrome
"""
from LinkedList import LinkedList, Node


class ReverseAndCompare:
    def __init__(self, head=None):
        self.head = head

    def reverseAndClone(self):
        pass

    def isEqual(self):
        pass

    def isPalindrome(self):
        pass


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

    # for testCase in TEST_CASES:
    #     head = tail = loopStartNode = None
    #     for i in testCase["input"]:
    #         new_node = Node(i)
    #         if testCase["loopStart"] == i:
    #             loopStartNode = new_node
    #
    #         if head is None:
    #             head = tail = new_node
    #         else:
    #             tail.next = new_node
    #             tail = new_node
    #
    #     if loopStartNode is not None:
    #         tail.next = loopStartNode
    #
    #     output = findLoop(head)
    #
    #     if output == testCase["output"]:
    #         print(f'TEST #{testCase["id"]} PASSED')
    #     else:
    #         print(f'TEST #{testCase["id"]} FAILED')
