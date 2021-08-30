#!/usr/bin/python3
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# https://www.algoexpert.io/questions/Youngest%20Common%20Ancestor

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_binary_tree(array, x, y):
    root = TreeNode(array[0])
    descendant_node = dict()
    if root.val == x:
        descendant_node['p'] = root
    if root.val == y:
        descendant_node['q'] = root

    queue = [(0, root)]

    while len(queue) > 0:
        (i, node) = queue.pop(0)
        li = i * 2 + 1
        ri = i * 2 + 2
        if li < len(array) and array[li] is not None:
            t = TreeNode(array[li])
            node.left = t
            queue.append((li, t))

            if t.val == x:
                descendant_node['p'] = t
            if t.val == y:
                descendant_node['q'] = t

        if ri < len(array) and array[ri] is not None:
            t = TreeNode(array[ri])
            node.right = t
            queue.append((ri, t))

            if t.val == x:
                descendant_node['p'] = t
            if t.val == y:
                descendant_node['q'] = t

    return root, descendant_node


# def preorder_traversal_recursive(root):
#     if root:
#         preorder_traversal_recursive(root.left)
#         preorder_traversal_recursive(root.right)
#         print(root.val)


def lowestCommonAncestor(root: TreeNode, descendantOne: TreeNode, descendantTwo: TreeNode) -> TreeNode:
    if root is None:
        return

    if root.val == descendantOne.val or root.val == descendantTwo.val:
        return root

    leftNode = lowestCommonAncestor(root.left, descendantOne, descendantTwo)
    rightNode = lowestCommonAncestor(root.right, descendantOne, descendantTwo)

    if leftNode is not None and rightNode is not None:
        return root
    elif leftNode is None and rightNode is not None:
        return rightNode
    elif leftNode is not None and rightNode is None:
        return leftNode
    else:
        return None


if __name__ == '__main__':
    # tree_array = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    # p = 5
    # q = 4
    tree_array = [1, 2]
    p = 1
    q = 2
    root_node, descendantNode = create_binary_tree(tree_array, p, q)
    lca = lowestCommonAncestor(root_node, descendantNode['p'], descendantNode['q'])
    print('LCA - ', lca.val)
