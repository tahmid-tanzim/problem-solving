#!/usr/bin/python3
# https://leetcode.com/problems/reverse-linked-list/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_list(node1, node2):
    if node1 is None:
        return node2
    if node2 is None:
        return node1

    if node1.val <= node2.val:
        node1.next = merge_list(node1.next, node2)
        return node1
    else:
        node2.next = merge_list(node1, node2.next)
        return node2


if __name__ == '__main__':
    l1 = ListNode(1)
    l3 = ListNode(3)
    l5_0 = ListNode(5)
    l7 = ListNode(7)

    l2 = ListNode(2)
    l4 = ListNode(4)
    l5_1 = ListNode(5)
    l6 = ListNode(6)
    l8 = ListNode(8)

    l1.next = l3
    l3.next = l5_0
    l5_0.next = l7

    l2.next = l4
    l4.next = l5_1
    l5_1.next = l6
    l6.next = l8

    j = merge_list(l1, l2)
    while j is not None:
        print(j.val)
        j = j.next
