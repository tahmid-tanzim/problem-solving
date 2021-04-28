#!/usr/bin/python3
"""
LinkedList length must be even number
"""
from LinkedList import LinkedList


def runner():
    ll = LinkedList()
    for i in range(1, 10, 2):
        ll.appendToTail(i)
    for i in range(2, 11, 2):
        ll.appendToTail(i)

    print('Before - ', ll)
    p1 = p2 = ll.__get__()

    while p1.next is not None and p1.next.next is not None:
        p1 = p1.next.next
        p2 = p2.next

    p2 = p2.next
    p1 = ll.__get__()

    while p2.next is not None:
        temp = p1.next
        p1.next = p2
        p1 = temp

        temp = p2.next
        p2.next = p1
        p2 = temp

    p1.next = p2
    print('After - ', ll)


if __name__ == "__main__":
    runner()



