#!/usr/bin/python3
# https://www.algoexpert.io/questions/Validate%20BST


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBstHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False
    return validateBstHelper(tree.left, minValue, tree.value) and validateBstHelper(tree.right, tree.value, maxValue)


def validateBst(tree):
    return validateBstHelper(tree, float('-inf'), float('inf'))


if __name__ == "__main__":
    # TODO
    pass
