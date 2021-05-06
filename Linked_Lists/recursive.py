#!/usr/bin/python3
"""
Traverse LinkedList Recursively
"""
from LinkedList import LinkedList, Node


def printASC(node: Node) -> None:
    if node is None:
        print('NULL', end='\n')
        return

    print(f'[{node}]', end='~>')
    printASC(node.next)


def printDESC(node: Node, stack: int) -> None:
    if node is None:
        return

    printDESC(node.next, stack + 1)
    print(f'[{node}]', end='~>NULL' if stack == 0 else '~>')


if __name__ == "__main__":
    ll = LinkedList()
    for i in range(1, 11):
        ll.appendToTail(i)

    printASC(ll.__get__())
    printDESC(ll.__get__(), 0)