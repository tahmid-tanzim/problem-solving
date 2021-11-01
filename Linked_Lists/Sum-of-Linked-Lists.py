#!/usr/bin/python3
# https://www.algoexpert.io/questions/Sum%20of%20Linked%20Lists
"""
  You're given two Linked Lists of potentially unequal length. Each Linked List
  represents a non-negative integer, where each node in the Linked List is a
  digit of that integer, and the first node in each Linked List always
  represents the least significant digit of the integer. Write a function that
  returns the head of a new Linked List that represents the sum of the integers
  represented by the two input Linked Lists.

  Each LinkedList node has an integer value as well as
  a next node pointing to the next node in the list or to
  None / null if it's the tail of the list. The
  value of each LinkedList node is always in the range
  of 0 - 9.

  Note: your function must create and return a new Linked List, and you're not
  allowed to modify either of the input Linked Lists.

Sample Input
linkedListOne = 2 -> 4 -> 7 -> 1
linkedListTwo = 9 -> 4 -> 5

Sample Output
1 -> 9 -> 2 -> 2
// linkedListOne represents 1742
// linkedListTwo represents 549
// 1742 + 549 = 2291
"""


# O(max(n, m)) time | O(max(n, m)) space
# where n is the length of the first Linked List and m is the length of the second Linked List
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    head = None
    tail = None
    carryOver = 0

    nodeOne = linkedListOne
    nodeTwo = linkedListTwo

    while nodeOne and nodeTwo:
        total = nodeOne.value + nodeTwo.value + carryOver
        tempNode = LinkedList(total % 10)
        carryOver = total // 10

        if head is None:
            tail = tempNode
            head = tail
        else:
            tail.next = tempNode
            tail = tail.next

        nodeOne = nodeOne.next
        nodeTwo = nodeTwo.next

    while nodeOne:
        total = nodeOne.value + carryOver
        tempNode = LinkedList(total % 10)
        carryOver = total // 10

        if head is None:
            tail = tempNode
            head = tail
        else:
            tail.next = tempNode
            tail = tail.next
        nodeOne = nodeOne.next

    while nodeTwo:
        total = nodeTwo.value + carryOver
        tempNode = LinkedList(total % 10)
        carryOver = total // 10

        if head is None:
            tail = tempNode
            head = tail
        else:
            tail.next = tempNode
            tail = tail.next
        nodeTwo = nodeTwo.next

    if carryOver:
        tail.next = LinkedList(carryOver)

    return head


if __name__ == "__main__":
    pass
