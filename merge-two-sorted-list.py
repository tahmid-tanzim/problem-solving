#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/merge-two-sorted-lists/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_lists(l1, l2):
    x, y = l1, l2
    i = ListNode(None)
    head = i
    while x is not None and y is not None:
        if x.val > y.val:
            i.next = ListNode(y.val)
            i = i.next
            y = y.next
        elif x.val < y.val:
            i.next = ListNode(x.val)
            i = i.next
            x = x.next
        elif x.val == y.val:
            i.next = ListNode(x.val)
            i = i.next
            i.next = ListNode(y.val)
            i = i.next
            x = x.next
            y = y.next
    if x is not None:
        i.next = x
    if y is not None:
        i.next = y
    return head.next


if __name__ == '__main__':
    l11 = ListNode(1)
    l12 = ListNode(2)
    l13 = ListNode(4)

    l11.next = l12
    l12.next = l13

    # i = l11
    # while i is not None:
    #     print(i.val)
    #     i = i.next

    ####################

    l21 = ListNode(1)
    l22 = ListNode(3)
    l23 = ListNode(4)
    l24 = ListNode(5)
    l25 = ListNode(6)

    l21.next = l22
    l22.next = l23
    l23.next = l24
    l24.next = l25

    # i = l21
    # while i is not None:
    #     print(i.val)
    #     i = i.next

    j = merge_two_lists(l11, l21)
    while j is not None:
        print(j.val)
        j = j.next
