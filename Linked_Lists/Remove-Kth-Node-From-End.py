#!/usr/bin/python3
# https://www.algoexpert.io/questions/Remove%20Kth%20Node%20From%20End
"""
  Write a function that takes in the head of a Singly Linked List and an integer
  k and removes the kth node from the end of the list.

  The removal should be done in place, meaning that the original data structure
  should be mutated (no new structure should be created).

  Furthermore, the input head of the linked list should remain the head of the
  linked list after the removal is done, even if the head is the node that's
  supposed to be removed. In other words, if the head is the node that's
  supposed to be removed, your function should simply mutate its
  value and next pointer.

  Note that your function doesn't need to return anything.

  You can assume that the input Linked List will always have at least two nodes
  and, more specifically, at least k nodes.

  Each LinkedList node has an integer value as well as
  a next node pointing to the next node in the list or to
  None / null if it's the tail of the list.

Sample Input
head = 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 // the head node with value 0
k = 4

Sample Output
// No output required.
// The 4th node from the end of the list (the node with value 6) is removed.
0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 9
"""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    first, last = head, head
    for _ in range(k):
        last = last.next

    if last is None:
        head.value = head.next.value
        head.next = head.next.next
        return

    while last.next is not None:
        first = first.next
        last = last.next

    first.next = first.next.next


if __name__ == "__main__":
    # TODO
    pass
