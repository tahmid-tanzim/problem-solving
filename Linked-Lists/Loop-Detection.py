#!/usr/bin/python3
"""
LinkedList - 2.8. Loop Detection
"""
from LinkedList import Node


def findLoop(head_node: Node):
    """
    O(n) time
    O(1) space
    """
    fast = slow = head_node
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if id(fast) == id(slow):
            break

    if fast is None or fast.next is None:
        return None

    slow = head_node
    while id(slow) != id(fast):
        slow = slow.next
        fast = fast.next

    return fast.data


if __name__ == "__main__":
    TEST_CASES = [
        {
            "id": 1,
            "input": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            "loopStart": 4,
            "output": 4
        },
        {
            "id": 2,
            "input": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
            "loopStart": None,
            "output": None
        }
    ]

    for testCase in TEST_CASES:
        head = tail = loopStartNode = None
        for i in testCase["input"]:
            newNode = Node(i)
            if testCase["loopStart"] == i:
                loopStartNode = newNode

            if head is None:
                head = tail = newNode
            else:
                tail.next = newNode
                tail = newNode

        if loopStartNode is not None:
            tail.next = loopStartNode

        output = findLoop(head)

        if output == testCase["output"]:
            print(f'TEST #{testCase["id"]} PASSED')
        else:
            print(f'TEST #{testCase["id"]} FAILED')
