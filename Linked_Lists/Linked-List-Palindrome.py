#!/usr/bin/python3
# https://www.algoexpert.io/questions/Linked%20List%20Palindrome
"""
  Write a function that takes in the head of a Singly Linked List and returns a
  boolean representing whether the linked list's nodes form a palindrome. Your
  function shouldn't make use of any auxiliary data structure.

  A palindrome is usually defined as a string that's written the same forward
  and backward. For a linked list's nodes to form a palindrome, their values
  must be the same when read from left to right and from right to left. Note
  that single-character strings are palindromes, which means that single-node
  linked lists form palindromes.

  Each LinkedList node has an integer value as well as
  a next node pointing to the next node in the list or to
  None / null if it's the tail of the list.

  You can assume that the input linked list will always have at least one node;
  in other words, the head will never be None / null.

Sample Input
head = 0 -> 1 -> 2 -> 2 -> 1 -> 0 // the head node with value 0

Sample Output
true
"""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time, O(n) space
class Solution1:
    def isPalindrome(self, head, tail):
        if tail is None:
            return {
                'output': True,
                'node': head
            }

        result = self.isPalindrome(head, tail.next)
        return {
            'output': result['output'] and result['node'].value == tail.value,
            'node': result['node'].next
        }

    def linkedListPalindrome(self, head):
        result = self.isPalindrome(head, head)
        return result['output']


# O(n) time, O(1) space
class Solution2:
    @staticmethod
    def reverseLinkedList(head):
        previousNode, currentNode = None, head

        while currentNode is not None:
            nextNode = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = nextNode

        return previousNode

    def linkedListPalindrome(self, head):
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        reversedSecondHalf = self.reverseLinkedList(slow)
        firstHalf = head

        while reversedSecondHalf is not None:
            if reversedSecondHalf.value != firstHalf.value:
                return False
            reversedSecondHalf = reversedSecondHalf.next
            firstHalf = firstHalf.next

        return True


if __name__ == "__main__":
    pass
