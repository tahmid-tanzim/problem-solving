#!/usr/bin/python3
"""
LinkedList - 2.4. Partition
"""
from LinkedList import LinkedList, Node


def partition(node: Node, x: int):
    """
    O(n) time
    O(1) space
    """
    head = tail = node
    while node is not None:
        next_node = node.next
        if node.data < x:
            node.next = head
            head = node
        else:
            tail.next = node
            tail = node
        node = next_node
    tail.next = None
    return head


if __name__ == "__main__":
    TEST_CASES = (
        {
            "id": 1,
            "input": [3, 5, 8, 5, 10, 2, 1],
            "x": 5,
            "output": [1, 2, 3, 5, 8, 5, 10]
        },
    )

    for testCase in TEST_CASES:
        ll = LinkedList()
        for i in testCase["input"]:
            ll.appendToTail(i)

        final_head = partition(ll.__get__(), testCase["x"])
        ll.__set__(final_head)
        print(ll)

        if ll == testCase["output"]:
            print(f'TEST #{testCase["id"]} PASSED')
        else:
            print(f'TEST #{testCase["id"]} FAILED')
