#!/usr/bin/python3
"""
LinkedList - 2.5. Sum List
"""
from LinkedList import LinkedList, Node


def length(node: Node) -> int:
    count: int = 0
    while node is not None:
        count += 1
        node = node.next
    return count


def insertBefore(head: Node, data: int) -> Node:
    node: Node = Node(data)
    if head is not None:
        node.next = head
    return node


def padList(node: Node, padding: int) -> Node:
    head_node: Node = node
    for _ in range(padding):
        head_node = insertBefore(head_node, 0)
    return head_node


def addListHelper(n1: Node, n2: Node):
    if n1 is None and n2 is None:
        return dict(carry=0, sumNode=None)

    obj: dict = addListHelper(n1.next, n2.next)
    total: int = n1.data + n2.data + obj["carry"]

    sumNode: Node = insertBefore(obj["sumNode"], total % 10)
    return dict(carry=total // 10, sumNode=sumNode)


def sumList(n1: Node, n2: Node):
    """
    Forward Order
    O(n) time
    O(n) space
    """
    len1: int = length(n1)
    len2: int = length(n2)

    if len1 < len2:
        n1 = padList(n1, len2 - len1)
    else:
        n2 = padList(n2, len1 - len2)

    result: dict = addListHelper(n1, n2)
    if result["carry"] == 0:
        return result["sumNode"]
    else:
        return insertBefore(result["sumNode"], result["carry"])


if __name__ == "__main__":
    TEST_CASES = (
        {
            "id": 1,
            "input1": [6, 1, 7],
            "input2": [2, 9, 5],
            "output": [9, 1, 2]
        },
        {
            "id": 2,
            "input1": [7, 1, 6],
            "input2": [5, 9, 2],
            "output": [1, 3, 0, 8]
        },
        {
            "id": 3,
            "input1": [1, 2, 3, 4],
            "input2": [9, 6, 3],
            "output": [2, 1, 9, 7]
        },
        {
            "id": 4,
            "input1": [5, 6],
            "input2": [1, 2, 3, 4],
            "output": [1, 2, 9, 0]
        }
    )

    for testCase in TEST_CASES:
        ll1 = LinkedList()
        ll2 = LinkedList()
        for i in testCase["input1"]:
            ll1.appendToTail(i)
        for i in testCase["input2"]:
            ll2.appendToTail(i)

        head = sumList(ll1.__get__(), ll2.__get__())
        linkList = LinkedList(head)

        if linkList == testCase["output"]:
            print(f'TEST #{testCase["id"]} PASSED')
        else:
            print(f'TEST #{testCase["id"]} FAILED')
