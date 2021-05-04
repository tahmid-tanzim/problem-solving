#!/usr/bin/python3
from Node import Node
from stack_exceptions import EmptyStackException


class Stack:
    def __init__(self, top: Node = None):
        self.__top = top

    def push(self, data: int) -> None:
        new_node = Node(data)
        new_node.next = self.__top
        self.__top = new_node

    def pop(self) -> int:
        if self.__top is None:
            raise EmptyStackException('Stack is empty.')
        data = self.__top.data
        self.__top = self.__top.next
        return data

    def peek(self) -> int:
        if self.__top is None:
            raise EmptyStackException('Stack is empty')
        return self.__top.data

    def isEmpty(self) -> bool:
        return self.__top is None
