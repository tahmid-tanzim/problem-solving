#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://www.hackerearth.com/practice/data-structures/trees/binary-and-nary-trees/tutorial/


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert(self, value, path=''):
        for c in path:
            pass

        if value <= self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    # def contains(self, value):
    #     if value == self.data:
    #         return True
    #     elif value <= self.data:
    #         if self.left is None:
    #             return False
    #         else:
    #             return self.left.contains(value)
    #     else:
    #         if self.right is None:
    #             return False
    #         else:
    #             return self.right.contains(value)

    def print_in_order(self):
        if self.left is not None:
            self.left.print_in_order()
        print(self.data)
        if self.right is not None:
            self.right.print_in_order()


if __name__ == '__main__':
    T, X = [int(x) for x in input().split()]
    root = Node(X)
    i = (T - 1) * 2
    while i > 0:
        path = input()
        value = int(input())
        print('Output: ', path, value)
        i -= 2
    # root = Node(10)
    # root.insert(5)
    # root.insert(15)
    # root.insert(8)
    # root.insert(17)
    # root.insert(12)
    # print('Is 8 exist: ', root.contains(8))
    # print('Is 12 exist: ', root.contains(12))
    # root.print_in_order()
