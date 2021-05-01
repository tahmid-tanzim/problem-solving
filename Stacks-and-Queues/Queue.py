#!/usr/bin/python3
from Node import Node


class NoSuchElementException(Exception):
    """Raised when the stack is empty"""
    pass


class Queue:
    def __init__(self, start: Node = None, end: Node = None):
        self.__start = start
        self.__end = end

    def add(self, data: int) -> None:
        new_node = Node(data)
        if self.__end is not None:
            self.__end.next = new_node
        self.__end = new_node
        if self.__start is None:
            self.__start = new_node

    def remove(self):
        if self.__start is None:
            raise NoSuchElementException('Queue is empty.')
        data = self.__start.data
        self.__start = self.__start.next
        if self.__start is None:
            self.__end = None
        return data

    def peek(self):
        if self.__start is None:
            raise NoSuchElementException('Stack is empty')
        return self.__start.data

    def isEmpty(self):
        return self.__start is None
