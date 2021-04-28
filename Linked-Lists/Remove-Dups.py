#!/usr/bin/python3
"""
LinkedList - 2.1. Remove Duplicates
"""
from LinkedList import LinkedList, Node


def removeDuplicate(node: Node):
    """
    using Hash Table
    O(n) time
    O(n) space
    """
    if node is None:
        return

    hash_table = dict([(node.data, True)])
    while node.next is not None:
        if node.next.data in hash_table:
            node.next = node.next.next
        else:
            hash_table[node.next.data] = True
            node = node.next


if __name__ == "__main__":
    TEST_CASES = (
        {
            "id": 1,
            "input": [4, 5, 9, 2, 4, 3, 9],
            "output": [4, 5, 9, 2, 3]
        },
        {
            "id": 2,
            "input": [1, 0, 1, 0],
            "output": [1, 0]
        },
        {
            "id": 3,
            "input": [5, 5, 5],
            "output": [5]
        },
        {
            "id": 4,
            "input": [1, 2, 3, 4, 5],
            "output": [1, 2, 3, 4, 5]
        }
    )

    for testCase in TEST_CASES:
        ll = LinkedList()
        for val in testCase["input"]:
            ll.appendToTail(val)

        removeDuplicate(ll.__get__())

        if ll == testCase["output"]:
            print(f'TEST #{testCase["id"]} PASSED')
        else:
            print(f'TEST #{testCase["id"]} FAILED')





