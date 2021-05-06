#!/usr/bin/python3
"""
LinkedList - 2.2. Return Kth to Last
i.e.
    k == 1 is last index
    k == 2 is second last index
"""
from LinkedList import LinkedList, Node


def kthLast(head: Node, k: int):
    """
    Iterative Solution
    O(n) time
    O(1) space
    """
    p1 = p2 = head
    for i in range(k):
        if p1 is None:
            return dict(data=None)
        p1 = p1.next

    while p1 is not None:
        p1 = p1.next
        p2 = p2.next
    return dict(data=p2.data)


def kthToLast(node: Node, k: int):
    """
    Recursive Solution
    O(n) time
    O(n) space
    """
    if node is None:
        return dict(index=0, data=None)

    obj = kthToLast(node.next, k)
    obj["index"] += 1
    if obj["index"] == k:
        return dict(index=obj["index"], data=node.data)
    else:
        return obj


if __name__ == "__main__":
    TEST_CASES = (
        {
            "id": 1,
            "input": [1, 2, 3, 4],
            "k": 2,
            "output": 3
        },
        {
            "id": 2,
            "input": [1, 2, 3, 4],
            "k": 1,
            "output": 4
        },
        {
            "id": 3,
            "input": [1, 2, 3, 4],
            "k": 5,
            "output": None
        }
    )

    for testCase in TEST_CASES:
        ll = LinkedList()
        for val in testCase["input"]:
            ll.appendToTail(val)

        o = kthLast(ll.__get__(), testCase["k"])

        if o["data"] == testCase["output"]:
            print(f'TEST #{testCase["id"]} PASSED')
        else:
            print(f'TEST #{testCase["id"]} FAILED')
