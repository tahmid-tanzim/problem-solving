class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''


def lca(root, v1, v2):
    if v1.info == v2.info:
        return v1
    else:
        lca(root.left, root.left.info, root.right.info)


# Enter your code here
tree = BinarySearchTree()
t = 6  # int(input())

arr = [4, 2, 3, 1, 7, 6]  # list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = [1, 7]  # list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print(ans.info)
