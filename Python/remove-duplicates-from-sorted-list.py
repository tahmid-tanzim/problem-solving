#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def delete_duplicates(head):
    h = head
    while h.next is not None:
        if h.val == h.next.val:
            h.next = h.next.next if h.next.next is not None else None
        else:
            h = h.next
    return h


if __name__ == '__main__':
    # [1, 1, 2]  || [1, 1, 2, 3, 3]

    node_head = None
    pointer = ListNode(None)
    for i in [1, 1, 2, 3, 3]:
        pointer.next = ListNode(i)
        if node_head is None:
            node_head = pointer.next
        pointer = pointer.next

    j = delete_duplicates(node_head)
    # j = head
    # while j is not None:
    #     print(j.val)
    #     j = j.next
