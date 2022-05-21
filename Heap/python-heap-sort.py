#!/usr/bin/python3
from heapq import heappush, heappop
import random


# HeapSort - Time O(n * log(n))
# Heap Push & Pop - Time O(log(n))
def heapsort(iterable, reverse=False):
    h = []
    n = len(iterable)
    direction = -1 if reverse else 1
    for value in iterable:
        heappush(h, value * direction)
    return [heappop(h) * direction for _ in range(n)]


if __name__ == "__main__":
    array = []

    for i in range(10):
        num = random.randint(10, 99)
        array.append(num)

    print("Array", array)
    print("HeapSort", heapsort(array, reverse=False))
