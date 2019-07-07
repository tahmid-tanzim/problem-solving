#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_elements(head, val):
    if head is None:
        return None

    # Remove from head
    while head.val == val:
        if head.next is not None:
            head = head.next
        else:
            return None

    i = head
    while i.next is not None:
        if i.next.val == val:
            i.next = i.next.next if i.next.next is not None else None
        else:
            i = i.next
    return head


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l6 = ListNode(6)
    l66 = ListNode(6)
    l666 = ListNode(6)
    l6666 = ListNode(6)

    # l6.next = l1
    # l1.next = l2
    # l2.next = l66
    # l66.next = l3
    # l3.next = l666
    # l666.next = l4
    # l4.next = l5
    # l5.next = l6666

    l6.next = l66
    l66.next = l666

    j = remove_elements(l6, 6)
    # j = l6
    while j is not None:
        print(j.val)
        j = j.next
