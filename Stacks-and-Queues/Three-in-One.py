#!/usr/bin/python3
"""
Stacks and Queues - 3.1. Three in One
"""
import unittest
from typing import List
from stack_exceptions import FullStackException, EmptyStackException, StackIndexOutOfRangeException


class FixedMultiStack:
    """
    Single Array to implement 3 Stack
    """
    __no_of_stack: int = 3

    def __init__(self, stack_size: int = 0):
        # Single Stack Size
        self.stack_size: int = stack_size
        self.array: List[int] = [-1] * (self.__no_of_stack * stack_size)
        self.top_index = [0] * self.__no_of_stack

    def __str__(self):
        return f'{self.array}'

    def __index_of(self, stack_index: int) -> int:
        if stack_index < 0 or stack_index >= self.__no_of_stack:
            raise StackIndexOutOfRangeException(f'Stack index is out of range. {stack_index}')
        offset = stack_index * self.stack_size
        return offset + self.top_index[stack_index]

    def push(self, stack_index: int, data: int) -> None:
        if self.isFull(stack_index):
            raise FullStackException(f'Stack is full. {stack_index}')
        index = self.__index_of(stack_index)
        self.array[index] = data
        self.top_index[stack_index] += 1

    def pop(self, stack_index: int) -> int:
        if self.isEmpty(stack_index):
            raise EmptyStackException(f'Stack is empty. {stack_index}')
        self.top_index[stack_index] -= 1
        index = self.__index_of(stack_index)
        data = self.array[index]
        self.array[index] = -1
        return data

    def peek(self, stack_index: int):
        if self.isEmpty(stack_index):
            raise EmptyStackException(f'Stack is empty. {stack_index}')
        index = self.__index_of(stack_index)
        return self.array[index - 1]

    def isEmpty(self, stack_index: int):
        if stack_index < 0 or stack_index >= self.__no_of_stack:
            raise StackIndexOutOfRangeException(f'Stack index is out of range. {stack_index}')
        return self.top_index[stack_index] == 0

    def isFull(self, stack_index: int):
        if stack_index < 0 or stack_index >= self.__no_of_stack:
            raise StackIndexOutOfRangeException(f'Stack index is out of range. {stack_index}')
        return self.top_index[stack_index] == self.stack_size


class TestFixedMultiStack(unittest.TestCase):
    def setUp(self):
        self.fms = FixedMultiStack(4)

    def test_is_full(self):
        self.assertFalse(self.fms.isFull(2))
        self.fms.push(2, 8)
        self.fms.push(2, 9)
        self.fms.push(2, 10)
        self.fms.push(2, 11)
        self.assertTrue(self.fms.isFull(2))

    def test_is_empty(self):
        self.assertTrue(self.fms.isEmpty(2))
        self.fms.push(2, 8)
        self.fms.push(2, 9)
        self.fms.push(2, 10)
        self.fms.push(2, 11)
        self.assertFalse(self.fms.isEmpty(2))

    def test_is_full_index_out_of_range_exception(self):
        stack_index = 3
        with self.assertRaises(StackIndexOutOfRangeException) as context:
            self.fms.isFull(stack_index)
        self.assertEqual(f'Stack index is out of range. {stack_index}', str(context.exception))

    def test_is_empty_index_out_of_range_exception(self):
        stack_index = -1
        with self.assertRaises(StackIndexOutOfRangeException) as context:
            self.fms.isEmpty(stack_index)
        self.assertEqual(f'Stack index is out of range. {stack_index}', str(context.exception))

    def test_pop_exception(self):
        stack_index = 2
        with self.assertRaises(EmptyStackException) as context:
            self.fms.pop(stack_index)
        self.assertEqual(f'Stack is empty. {stack_index}', str(context.exception))

    def test_peek_exception(self):
        stack_index = 1
        with self.assertRaises(EmptyStackException) as context:
            self.fms.peek(1)
        self.assertEqual(f'Stack is empty. {stack_index}', str(context.exception))

    def test_push(self):
        self.fms.push(2, 8)
        self.fms.push(2, 9)
        self.fms.push(2, 10)
        self.fms.push(2, 11)
        val = self.fms.peek(2)
        self.assertEqual(val, 11)

    def test_pop_single_stack(self):
        stack_index = 1
        self.fms.push(stack_index, 4)
        self.fms.push(stack_index, 5)
        self.fms.push(stack_index, 6)
        self.fms.push(stack_index, 7)
        val = self.fms.pop(stack_index)
        self.assertEqual(val, 7)
        val = self.fms.pop(stack_index)
        self.assertEqual(val, 6)
        val = self.fms.pop(stack_index)
        self.assertEqual(val, 5)
        val = self.fms.pop(stack_index)
        self.assertEqual(val, 4)
        with self.assertRaises(EmptyStackException) as context:
            val = self.fms.pop(stack_index)
            self.assertEqual(f'Stack is empty. {stack_index}', str(context.exception))
            self.assertEqual(val, None)

    def test_pop_multi_stack(self):
        self.fms.push(0, 0)
        self.fms.push(0, 1)
        self.fms.push(0, 2)
        self.fms.push(1, 4)
        self.fms.push(1, 5)
        self.fms.push(2, 8)

        val = self.fms.pop(0)
        self.assertEqual(val, 2)
        val = self.fms.pop(0)
        self.assertEqual(val, 1)
        val = self.fms.pop(1)
        self.assertEqual(val, 5)
        val = self.fms.pop(2)
        self.assertEqual(val, 8)

        with self.assertRaises(EmptyStackException) as context:
            val = self.fms.pop(2)
            self.assertEqual(f'Stack is empty. {2}', str(context.exception))
            self.assertEqual(val, None)

    def test_peek(self):
        self.fms.push(0, 0)
        self.fms.push(0, 1)
        self.fms.push(0, 2)
        self.fms.push(1, 4)
        self.fms.push(1, 5)
        self.fms.push(2, 8)

        val = self.fms.peek(0)
        self.assertEqual(val, 2)
        val = self.fms.peek(1)
        self.assertEqual(val, 5)
        val = self.fms.peek(2)
        self.assertEqual(val, 8)


if __name__ == "__main__":
    unittest.main()
