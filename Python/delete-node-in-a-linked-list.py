#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/delete-node-in-a-linked-list/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_node(node):
    node.val = node.next.val
    node.next = node.next.next


if __name__ == '__main__':
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1 = ListNode(1)
    l9 = ListNode(9)

    l4.next = l5
    l5.next = l1
    l1.next = l9

    delete_node(l1)
    j = l4
    while j is not None:
        print(j.val)
        j = j.next
