#!/usr/bin/python3
# https://www.algoexpert.io/questions/Remove%20Duplicates%20From%20Linked%20List
"""
INPUT = 1~>1~>3~>4~>4~>4~>5~>6~>6
OUTPUT = 1~>3~>4~>5~>6
"""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time
# O(1) space
def removeDuplicatesFromLinkedList(linkedList):
    node = linkedList
    while node.next is not None:
        if node.value == node.next.value:
            node.next = node.next.next
        else:
            node = node.next
    return linkedList


if __name__ == "__main__":
    # TODO
    pass
