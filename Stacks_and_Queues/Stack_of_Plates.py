#!/usr/bin/python3
"""
Stacks and Queues - 3.3. Stack of Plates
"""
import unittest
from stack_exceptions import EmptyStackException


class Node:
    def __init__(self, data):
        self.data = data
        self.above = None
        self.below = None

    def __str__(self):
        return f'{self.data}'


def join(above: Node, below: Node):
    if below is not None:
        below.above = above
    if above is not None:
        above.below = below


class Stack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.top = None
        self.bottom = None
        self.size: int = 0

    def isFull(self):
        return self.capacity == self.size

    def push(self, v: int) -> bool:
        if self.size >= self.capacity:
            return False

        self.size += 1
        n = Node(v)
        if self.size == 1:
            self.bottom = n
        join(n, self.top)
        self.top = n
        return True

    def pop(self) -> int:
        t = self.top
        self.top = self.top.below
        self.size -= 1
        return t.data

    def isEmpty(self) -> bool:
        return self.size == 0

    def removeBottom(self):
        b = self.bottom
        self.bottom = self.bottom.above
        if self.bottom is not None:
            self.bottom.below = None
        self.size -= 1
        return b.data


class SetOfStacks:
    def __init__(self, capacity: int = 0):
        self.stacks = list()
        self.capacity = capacity

    def push(self, data) -> None:
        last = self.get_last_stack()
        if last is not None and not last.isFull():
            last.push(data)
        else:
            stack = Stack(self.capacity)
            stack.push(data)
            self.stacks.append(stack)

    def pop(self) -> Node:
        last = self.get_last_stack()
        if last is None:
            raise EmptyStackException('Stack is empty.')
        v = last.pop()
        if last.size == 0:
            self.stacks.pop()
        return v

    def get_last_stack(self):
        if len(self.stacks) == 0:
            return None
        return self.stacks[-1]

    def isEmpty(self):
        last = self.get_last_stack()
        return last is None or last.isEmpty()

    def leftShift(self, index, removeTop):
        stack = self.stacks[index]
        removed_item = stack.pop() if removeTop else stack.removeBottom()

        if stack.isEmpty():
            self.stacks = self.stacks[:index] + self.stacks[index + 1:]
        elif len(self.stacks) > index + 1:
            v = self.leftShift(index + 1, False)
            stack.push(v)

        return removed_item

    def popAt(self, index: int):
        return self.leftShift(index, True)


class TestSetOfStacks(unittest.TestCase):
    def setUp(self):
        self.sos = SetOfStacks(4)

    def test_is_empty(self):
        self.assertTrue(self.sos.isEmpty())
        self.sos.push(10)
        self.assertFalse(self.sos.isEmpty())

    def test_push(self):
        for i in range(1, 6):
            self.sos.push(i)

        for i in range(5, 0, -1):
            val = self.sos.pop()
            self.assertEqual(val, i)

        with self.assertRaises(EmptyStackException) as context:
            val = self.sos.pop()
            self.assertEqual('Stack is empty', str(context.exception))
            self.assertEqual(val, None)

    def test_pop_at(self):
        for i in range(12):
            self.sos.push(i)

        val = self.sos.popAt(0)
        self.assertEqual(val, 3)
        val = self.sos.popAt(1)
        self.assertEqual(val, 8)

    def test_pop_at_exception(self):
        for i in range(6):
            self.sos.push(i)

        val = self.sos.popAt(0)
        self.assertEqual(val, 3)
        val = self.sos.popAt(0)
        self.assertEqual(val, 4)
        val = self.sos.popAt(0)
        self.assertEqual(val, 5)
        val = self.sos.popAt(0)
        self.assertEqual(val, 2)
        val = self.sos.popAt(0)
        self.assertEqual(val, 1)
        val = self.sos.popAt(0)
        self.assertEqual(val, 0)
        with self.assertRaises(IndexError) as context:
            val = self.sos.popAt(0)
            self.assertEqual('IndexError: list index out of range', str(context.exception))
            self.assertEqual(val, None)


if __name__ == "__main__":
    unittest.main()
