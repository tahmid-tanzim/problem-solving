#!/usr/bin/python3
"""
Python Collection deque
"""
from collections import deque


class DoubleEndedQueue:
    def __init__(self, queue=[]):
        self.queue = queue

    def __str__(self):
        return f"DoubleEndedQueue({self.queue})"

    def append(self, data):
        self.queue.append(data)
    
    def pop(self):
        return self.queue.pop()

    def appendleft(self, data):
        self.queue.insert(0, data)

    def popleft(self):
        return self.queue.pop(0)


if __name__ == "__main__":
    q1 = deque([1, 2, 3])
    q1.append(4)
    q1.appendleft(0)
    print(q1)
    rightValue = q1.pop()
    leftValue = q1.popleft()
    print(leftValue, rightValue)
    print(q1)
    ##############################
    q2 = DoubleEndedQueue([1, 2, 3])
    q2.append(4)
    q2.appendleft(0)
    print(q2)
    rightValue = q2.pop()
    leftValue = q2.popleft()
    print(leftValue, rightValue)
    print(q2)
