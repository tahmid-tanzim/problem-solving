#!/usr/bin/python3
"""
Stacks and Queues - 3.5. Sort Stack
"""
from StackDS import Stack


def sortStack(s: Stack):
    r = Stack()
    while not s.isEmpty():
        temp = s.pop()
        while not r.isEmpty() and r.peek() > temp:
            s.push(r.pop())
        r.push(temp)

    while not r.isEmpty():
        temp = r.pop()
        print(temp)
        s.push(temp)
    return s


if __name__ == "__main__":
    stack = Stack()
    stack.push(3)
    stack.push(12)
    stack.push(9)
    stack.push(1)
    stack.push(15)
    stack.push(6)

    stack = sortStack(stack)

