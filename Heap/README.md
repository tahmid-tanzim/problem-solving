# Heap - Heap Sort - Heapify - Priority Queues

1. If a Node is at index ~> i
2. Then left child is at index ~> 2i + 1
3. Then right child is at index ~> 2i + 2
4. Then parent is at index ~> i // 2

- Heap is a Complete Binary Tree
- Every Full Binary Tree is a Complete Binary Tree.
- Height of a Complete Binary Tree is ~> log(n)
- Max Heap - Parent Nodes value will be >= child node
- Min Heap - Parent Nodes value will be <= child node


## 1.Insert into Max Heap
#### 1.1. Append new value in the heap array
```python3
new_value = 60
heap = [50, 30, 20, 15, 10, 8, 16]
```
#### 1.2. Compare with Parent (up)
If the value is greater than parent then swap
proceed this process until parent index is equal 0

*Time Complexity* - Maximum swap will be height of the complete binary tree.
So the Time Complexity of inserting a value from MAX or MIN Heap is minimum `O(1)` and maximum `O(log(n))`.


## 2.Delete from Max Heap
*Note* - Only Root element can be deleted from Max or Min Heap.
#### 2.1. Copy first value or root element from Heap
```python3
heap = [50, 30, 20, 15, 10, 8, 16]
del_value = heap[0]
```
#### 2.2. Copy the last element to the first position (down)
```python3
del_value = 50
heap = [16, 30, 20, 15, 10, 8, None]
```
Compare and find the max value of two child. Then swap if parent's value is less than max child.
Repeat this task until last of heap.

*Time Complexity* - Maximum swap will be height of the complete binary tree.
So the Time Complexity of deleting a value from MAX or MIN Heap is minimum `O(1)` and maximum `O(log(n))`.


## 3. Heap Sort
#### 3.1. From given set of elements Create a HEAP
*Time Complexity* of a Heap Creation is `O(n log(n))` 
#### 3.2. Delete all the elements from the HEAP
`Note` - Deleting all the element from Max Heap and Put the value in empty space will sort the array in ascending order.


## 4. Heapify
Heapify is a process of creating a Heap from end
*Time Completion* of heapify if `O(n)`
```python3
array = [10, 20, 15, 12, 40, 25, 18]
```
For Max Heap, from last index to 0 check if children NOT exists then its considered as Heap. Else if children exists then adjust with children (shift down) until the sub tree is Max / Min Heap.


## 5. Priority Queue
#### 5.1. If small number is higher priority 
Then Create & Delete Min Heap
#### 5.2. If large number is higher priority 
Then Create & Delete Max Heap