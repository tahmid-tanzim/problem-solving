#!/usr/bin/python3
"""
Stacks and Queues - 3.2.
"""
from Node import Node
from StackDS import Stack


class StackMin(Stack):
    def __init__(self, top: Node = None):
        self.__minValueStack = Stack()
        super().__init__(top)

    def minimum(self):
        if self.__minValueStack.isEmpty():
            return float('inf')
        else:
            return self.__minValueStack.peek()

    def push(self, data: int) -> None:
        if data < self.minimum():
            self.__minValueStack.push(data)
        super().push(data)

    def pop(self) -> Node:
        data = super().pop()
        if data == self.minimum():
            self.__minValueStack.pop()
        return data


if __name__ == "__main__":
    sm = StackMin()
    sm.push(5)
    sm.push(6)
    sm.push(3)
    sm.push(7)
    sm.pop()
    sm.pop()
    print(f'Top - {sm.peek()} | Min - {sm.minimum()}')
