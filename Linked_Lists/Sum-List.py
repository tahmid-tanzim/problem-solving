#!/usr/bin/python3
"""
LinkedList - 2.5. Sum List
"""
from LinkedList import LinkedList, Node


def sumList(n1: Node, n2: Node):
    """
    Reverse Order
    O(n) time
    O(n) space
    """
    result = LinkedList()
    carry = 0
    while n1 is not None and n2 is not None:
        total = n1.data + n2.data + carry
        carry = total // 10
        result.appendToTail(total % 10)
        n1 = n1.next
        n2 = n2.next

    while n1 is not None:
        total = n1.data + carry
        carry = total // 10
        result.appendToTail(total % 10)
        n1 = n1.next

    while n2 is not None:
        total = n2.data + carry
        carry = total // 10
        result.appendToTail(total % 10)
        n2 = n2.next

    if carry:
        result.appendToTail(carry)

    return result


if __name__ == "__main__":
    TEST_CASES = (
        {
            "id": 1,
            "input1": [7, 1, 6],
            "input2": [5, 9, 2],
            "output": [2, 1, 9]
        },
        {
            "id": 2,
            "input1": [6, 1, 7],
            "input2": [2, 9, 5],
            "output": [8, 0, 3, 1]
        },
        {
            "id": 3,
            "input1": [4, 3, 2, 1],
            "input2": [3, 6, 9],
            "output": [7, 9, 1, 2]
        },
        {
            "id": 4,
            "input1": [6, 5],
            "input2": [4, 3, 2, 1],
            "output": [0, 9, 2, 1]
        }
    )

    for testCase in TEST_CASES:
        ll1 = LinkedList()
        ll2 = LinkedList()
        for val in testCase["input1"]:
            ll1.appendToTail(val)
        for val in testCase["input2"]:
            ll2.appendToTail(val)

        linkList = sumList(ll1.__get__(), ll2.__get__())

        if linkList == testCase["output"]:
            print(f'TEST #{testCase["id"]} PASSED')
        else:
            print(f'TEST #{testCase["id"]} FAILED')
