#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/remove-linked-list-elements/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_elements(head, val):
    if head is None:
        return head

    # Remove from head
    while head.val == val:
        head = head.next

    i = head
    while i.next is not None:
        print(i.val, i.next, i.next.next, end='\n\n')
        if i.next.val == val:
            pass
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

    l6.next = l1
    l1.next = l2
    l2.next = l66
    l66.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l666

    j = remove_elements(l1, 6)
    # j = a
    # while j is not None:
    #     print(j.val)
    #     j = j.next
