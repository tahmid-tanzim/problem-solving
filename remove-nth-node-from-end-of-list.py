#!/usr/bin/python3
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


class ListNode:
    def __init__(self, v=0, n=None):
        self.val = v
        self.next = n

    def __str__(self):
        return self.val


# def remove_nth_from_end(head, n):
#     current_pointer = nth_pointer = head
#     i = 0
#     while current_pointer.next is not None:
#         current_pointer = current_pointer.next
#         i += 1
#         if i >= n:
#             nth_pointer = nth_pointer.next
#             i = 0
#     print('\nnth Pointer: ', nth_pointer.val, end='\n\n')
#     return head


def remove_nth(head, n):
    current_pointer = head
    i = 0
    while current_pointer is not None:
        if i == n:
            current_pointer.next = current_pointer.next.next
            break
        current_pointer = current_pointer.next
        i += 1
    return head


def generate_linked_list(l):
    pointer = None
    for i in reversed(l):
        pointer = ListNode(i, pointer)
    return pointer


if __name__ == '__main__':
    h = generate_linked_list([1, 2, 3, 4, 5])
    # j = remove_nth_from_end(h, 4)
    j = remove_nth(h, 2)

    # h = generate_linked_list([1, 2])
    # j = remove_nth_from_end(h, 1)
    while j is not None:
        print(j.val, end='~>')
        j = j.next
