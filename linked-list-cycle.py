#!/usr/bin/python3
# https://leetcode.com/problems/linked-list-cycle/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head):
    id_freq = {}
    while head is not None:
        if id(head) in id_freq:
            return True
        else:
            id_freq[id(head)] = 1
        head = head.next
    return False


if __name__ == '__main__':

    l0 = ListNode(3)
    l1 = ListNode(2)
    l2 = ListNode(0)
    l3 = ListNode(-4)

    l0.next = l1
    l1.next = l2
    l2.next = l3
    l3.next = l1

    ######################

    # l0 = ListNode(1)
    # l1 = ListNode(2)

    # l0.next = l1
    # l1.next = l0


    print(has_cycle(l0))
    # j = l0
    # counter = 0
    # while j is not None:
    #     print(j.val)
    #     j = j.next
    #     if counter == 8:
    #         break
    #     counter += 1
