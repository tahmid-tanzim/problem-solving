#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/middle-of-the-linked-list/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def middle_node(head):
    count = 0
    middle_pointer = 0
    middle_list_node = head
    while head is not None:
        count += 1
        if count % 2 == 0:
            temp_middle_pointer = round(count / 2) + 1
        else:
            temp_middle_pointer = round(count / 2)

        if temp_middle_pointer > middle_pointer:
            middle_pointer = temp_middle_pointer
            middle_list_node = middle_list_node.next

        head = head.next
    return middle_list_node


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    # l4 = ListNode(4)
    # l5 = ListNode(5)
    # l6 = ListNode(6)

    l1.next = l2
    l2.next = l3
    # l3.next = l4
    # l4.next = l5
    # l5.next = l6

    output = middle_node(l1)
    print(output.val)

