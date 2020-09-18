#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/reverse-linked-list/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def reverse_list(head):
    if head is None:
        return head

    output = ListNode(head.val)
    head = head.next
    while head is not None:
        temp = ListNode(head.val)
        temp.next = output
        output = temp
        head = head.next
    return output


def reverse_list_recursion(node):
    if node is None:
        return None
    if node.next is None:
        return node

    head_node = reverse_list_recursion(node.next)
    node.next.next = node
    node.next = None
    return head_node


if __name__ == '__main__':
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    # l6 = ListNode(6)

    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    # l5.next = l6

    j = reverse_list_recursion(l1)
    while j is not None:
        print(j.val)
        j = j.next
