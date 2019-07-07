#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/add-two-numbers/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    head = ListNode(None)
    pointer = ListNode(None)
    carry_over = 0
    while l1 is not None or l2 is not None:
        added_val = (l1.val if l1 is not None else 0) + (l2.val if l2 is not None else 0) + carry_over
        pointer.next = ListNode(added_val % 10)
        if head.next is None:
            head.next = pointer.next
        pointer = pointer.next
        carry_over = added_val // 10
        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next

    if carry_over > 0:
        pointer.next = ListNode(carry_over)

    return head.next


if __name__ == '__main__':
    # l3 = ListNode(3)
    # l41 = ListNode(4)
    # l21 = ListNode(2)
    #
    # l42 = ListNode(4)
    # l6 = ListNode(6)
    # l5 = ListNode(5)

    l3 = ListNode(9)
    l41 = ListNode(9)
    l21 = ListNode(9)

    l42 = ListNode(9)
    l6 = ListNode(9)
    l5 = ListNode(9)

    l21.next = l41
    l41.next = l3

    l5.next = l6
    l6.next = l42

    # l9 = ListNode(9)
    # l9.next = l21

    j = add_two_numbers(l21, l5)
    # j = add_two_numbers(l5, l9)
    # j = l5
    while j is not None:
        print(j.val)
        j = j.next

    # 7 -> 0 -> 8
