#!/usr/bin/python3
"""
LinkedList - 2.7. Intersection
"""
from LinkedList import LinkedList, Node


def findIntersection(nodeOne: Node, nodeTwo: Node) -> Node:
    """
    O(a + b) time
    O(1) space
    """
    # 1. Traverse Two List to Find the Length
    n1 = nodeOne
    length1: int = 1
    while n1.next is not None:
        length1 += 1
        n1 = n1.next

    n2 = nodeTwo
    length2: int = 1
    while n2.next is not None:
        length2 += 1
        n2 = n2.next

    # 2. Check is both Tail Node is same, If NOT return None
    if id(n1) != id(n2):
        return None

    # 3. Initiate both the pointer from head
    n1, n2 = nodeOne, nodeTwo

    # 4. By pass the extra node from length difference
    if length1 < length2:
        for _ in range(length2 - length1):
            n2 = n2.next

    if length1 > length2:
        for _ in range(length1 - length2):
            n1 = n1.next

    # 5. Traverse both the list to find the joining Node
    while n1 is not None and n2 is not None:
        if id(n1) == id(n2):
            return n1
        n1 = n1.next
        n2 = n2.next


if __name__ == "__main__":
    TEST_CASES = [
        {
            "id": 1,
            "input1": [3, 1, 5, 9],
            "input2": [4, 6],
            "common": [7, 2, 1]
        },
        {
            "id": 2,
            "input1": [3, 1, 5, 9, 7, 2, 1],
            "input2": [4, 6, 7, 2, 1],
            "common": None
        }
    ]

    for testCase in TEST_CASES:
        list1 = LinkedList()
        for i in testCase["input1"]:
            list1.appendToTail(i)

        list2 = LinkedList()
        for i in testCase["input2"]:
            list2.appendToTail(i)

        commonList = None
        if testCase["common"] is not None:
            commonList = LinkedList()
            for i in testCase["common"]:
                commonList.appendToTail(i)
            list1.appendNodeToTail(commonList.__get__())
            list2.appendNodeToTail(commonList.__get__())

        joiningNode = findIntersection(list1.__get__(), list2.__get__())

        if (joiningNode is None and commonList is None) or (id(joiningNode) == id(commonList.__get__())):
            print(f'TEST #{testCase["id"]} PASSED')
        else:
            print(f'TEST #{testCase["id"]} FAILED')
