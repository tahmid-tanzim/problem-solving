#!/usr/bin/python3


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swap_pairs(head: ListNode) -> ListNode:
    if head is None:
        return
    if head.next is None:
        return head

    temp = head.val
    head.val = head.next.val
    head.next.val = temp

    head.next.next = swap_pairs(head.next.next)

    return head


if __name__ == '__main__':
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n6 = ListNode(6)

    h = n1
    h.next = n2
    h.next.next = n3
    h.next.next.next = n4
    h.next.next.next.next = n5
    h.next.next.next.next.next = n6

    # temp = head.val
    # head.val = head.next.val
    # head.next.val = temp

    h = swap_pairs(h)

    while h is not None:
        print('VALUE: ', h.val)
        h = h.next

    print('END: ', h)
