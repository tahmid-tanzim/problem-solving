#!/usr/bin/python3
# https://www.algoexpert.io/questions/Find%20Closest%20Value%20In%20BST
"""
TREE
           10
        /     \
      5        15
    /  \     /    \
   2    5  13     22
 /           \
1             14

TARGET = 12
OUTPUT = 13

Description - A valid BST node is `left.values < node.value <= right.values`
"""


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Recursive Solution
def findClosestValueInBst1(tree, target):
    if tree.value == target:
        return target

    if target < tree.value:
        my_diff = tree.value - target
        if tree.left is not None:
            child_value = findClosestValueInBst1(tree.left, target)
            child_diff = abs(child_value - target)
            return child_value if child_diff < my_diff else tree.value
        else:
            return tree.value

    if target > tree.value:
        my_diff = target - tree.value
        if tree.right is not None:
            child_value = findClosestValueInBst1(tree.right, target)
            child_diff = abs(child_value - target)
            return child_value if child_diff < my_diff else tree.value
        else:
            return tree.value


# Recursive Solution
def findClosestValueInBst2(tree, target):
    return findClosestValueInBstHelper2(tree, target, tree.value)


def findClosestValueInBstHelper2(tree, target, closest):
    # Base Condition
    if tree is None:
        return closest

    # Set Minimum Closest
    if abs(target - tree.value) < abs(target - closest):
        closest = tree.value

    # Traverse BST
    if target < tree.value:
        return findClosestValueInBstHelper2(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper2(tree.right, target, closest)
    else:
        return closest


# Iterative Solution
def findClosestValueInBst3(tree, target):
    return findClosestValueInBstHelper3(tree, target, tree.value)


def findClosestValueInBstHelper3(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        # Set Minimum Closest
        if abs(target - currentNode.value) < abs(target - closest):
            closest = currentNode.value
        # Traverse BST
        if target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest


if __name__ == "__main__":
    # TODO Create BST and Find closest value in BST
    pass
