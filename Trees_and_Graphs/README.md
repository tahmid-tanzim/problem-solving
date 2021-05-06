# Trees and Graphs

## 1. Types of Trees
### Binary Tree
A binary tree is a tree in which each node has up to two children.

### Binary Search Tree
A binary search tree is a binary tree in which every node fits a specific ordering property.
```shell
all left descendents <= n < all right descendents
```
This must be true for each node n.

### Balanced vs Unbalanced Tree
To ensure `O(log n)` times for insert and find. Two common types of balanced trees are [Red-Black Tree](https://www.geeksforgeeks.org/red-black-tree-set-1-introduction-2/) and [AVL tree](https://www.geeksforgeeks.org/avl-tree-set-1-insertion/)

### Complete Binary Tree
A complete binary tree is a binary tree in which every level of the tree is fully filled, except the last level.
>[Heap](../Heap/README.md) is a Complete Binary Tree

### Full Binary Tree
A full binary tree is a binary tree in which every node has either zero or two children. That is, no nodes have only one child.

### Perfect Binary Tree
A perfect binary tree is one that is both full and complete. All leaf nodes will be at the same level, and this level has the maximum number of nodes. a perfect tree must have exactly `2^k - 1` nodes.

## 2. Binary Tree Traversal
* In-Order Traversal
* Pre-Order Traversal
* Post-Order Traversal

## 3. Binary Heaps 
[MIN & MAX Heap](../Heap/README.md)

## 4. Tries (Prefix Trees)
A trie is a variant of an n-ary tree in which characters are stored at each node. Each path down the tree may represent a word.

## 5. Graphs
* A tree is a connected graph without cycles.
* A graph can be directed or undirected.
* A graph might consist of multiple subgraphs. If there is a path between every pair of vertices, it is called a "connected graph".
* A graph can also have cycles (or not). An "Acyclic graph" is one without cycles.

### Graph Search
* BFS 
* DFS