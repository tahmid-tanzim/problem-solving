#!/usr/bin/python3
# https://www.algoexpert.io/questions/Find%20Loop
"""
  Write a function that takes in the head of a Singly Linked List that contains
  a loop (in other words, the list's tail node points to some node in the list
  instead of None / null). The function should return
  the node (the actual node--not just its value) from which the loop originates
  in constant space.

  Each LinkedList node has an integer value as well as
  a next node pointing to the next node in the list.

Sample Input
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 // the head node with value 0
                           ^         v
                           9 <- 8 <- 7

Sample Output
4 -> 5 -> 6 // the node with value 4
^         v
9 <- 8 <- 7
"""
from LinkedList import Node


# O(n) time, O(1) space
def findLoop(head_node: Node):
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
