#!/usr/bin/python3
"""
LinkedList - 2.3. Delete Middle Node
"""
from LinkedList import LinkedList, Node


def removeNode(node: Node) -> bool:
    if node is None or node.next is None:
        return False

    nextNode: Node = node.next
    node.data = nextNode.data
    node.data = nextNode.next
    return True


if __name__ == "__main__":
    TEST_CASES = (
        {
            "id": 1,
            "input": [1, 2, 3, 4, 5],
            "output": [1, 2, 4, 5]
        },
        {
            "id": 2,
            "input": [1, 2, 3, 4],
            "output": [1, 3, 4]
        },
        {
            "id": 3,
            "input": [1, 2],
            "output": [2]
        },
        {
            "id": 4,
            "input": [1],
            "output": []
        }
    )

    for testCase in TEST_CASES:
        ll = LinkedList()
        for val in testCase["input"]:
            ll.appendToTail(val)

        ll.deleteMiddle()

        if ll == testCase["output"]:
            print(f'TEST #{testCase["id"]} PASSED')
        else:
            print(f'TEST #{testCase["id"]} FAILED')
