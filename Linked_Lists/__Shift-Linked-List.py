#!/usr/bin/python3
# https://www.algoexpert.io/questions/Shift%20Linked%20List
"""
Write a function that takes in the head of a Singly Linked List and an integer
k, shifts the list in place (i.e., doesn't create a brand new
list) by k positions, and returns its new head.

Shifting a Linked List means moving its nodes forward or backward and wrapping
them around the list where appropriate. For example, shifting a Linked List
forward by one position would make its tail become the new head of the linked list.

Whether nodes are moved forward or backward is determined by whether
k is positive or negative.

Each LinkedList node has an integer value as well as
a next node pointing to the next node in the list or to
None / null if it's the tail of the list.

You can assume that the input Linked List will always have at least one node;
in other words, the head will never be None / null.

Sample Input
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 // the head node with value 0
k = 2

Sample Output
4 -> 5 -> 0 -> 1 -> 2 -> 3 // the new head node with value 4
"""


# O(n) time | O(1) space
# where n is the number of nodes in the Linked List
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    if k == 0:
        return head

    if k < 0:
        k *= -1

    fast = head
    slow = head
    while fast is not None:
        if fast.next is None:
            break
        slow = slow.next
        print('slow - ', slow.value)
        i = 0
        while i < k and fast is not None:
            fast = fast.next
            i += 1
    return None


if __name__ == '__main__':
    pass
