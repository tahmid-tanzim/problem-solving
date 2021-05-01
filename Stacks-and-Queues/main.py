#!/usr/bin/python3
from Stack import Stack
from Queue import Queue


if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(6)
    try:
        val = s.pop()
        print(val)
    except Exception as ex:
        print(ex)

    print(s.peek())
    print(s.isEmpty())

    q = Queue()
    q.add(5)
    q.add(6)
    try:
        val = q.remove()
        print(val)
    except Exception as ex:
        print(ex)

    print(q.peek())
    print(q.isEmpty())


