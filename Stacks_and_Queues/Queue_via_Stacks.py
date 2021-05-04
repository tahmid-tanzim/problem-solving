#!/usr/bin/python3
"""
Stacks and Queues - 3.4. Queue via Stacks
"""
from StackDS import Stack
from stack_exceptions import EmptyStackException, NoSuchElementException


class MyQueue:
    def __init__(self):
        self.stackDESC = Stack()
        self.stackASC = Stack()
        self.switch = True

    def add(self, data: int) -> None:
        if not self.switch:
            while not self.stackDESC.isEmpty():
                value = self.stackDESC.pop()
                self.stackASC.push(value)
            self.switch = True
        self.stackASC.push(data)

    def remove(self):
        if self.switch:
            while not self.stackASC.isEmpty():
                value = self.stackASC.pop()
                self.stackDESC.push(value)
            self.switch = False
        try:
            return self.stackDESC.pop()
        except EmptyStackException as ex:
            print(ex)
            raise NoSuchElementException('Queue is empty.')

    def peek(self):
        if self.switch:
            while not self.stackASC.isEmpty():
                value = self.stackASC.pop()
                self.stackDESC.push(value)
            self.switch = False
        try:
            return self.stackDESC.peek()
        except EmptyStackException as ex:
            print(ex)
            raise NoSuchElementException('Queue is empty.')

    def isEmpty(self):
        return self.stackASC.isEmpty() if self.switch else self.stackDESC.isEmpty()


if __name__ == "__main__":
    mq = MyQueue()
    mq.add(1)
    mq.add(2)
    mq.add(3)
    v = mq.remove()
    print(v)
    mq.add(4)

    v = mq.remove()
    print(v)
    v = mq.remove()
    print(v)
    v = mq.peek()
    print(v)
    print(mq.isEmpty())
