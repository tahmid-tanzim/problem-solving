#!/usr/bin/python3

# Time Complexity - O(n)
def cyclicSort(array):
    i = 0
    while i < len(array):
        correctIdx = array[i] - 1
        if correctIdx != i:
            array[i], array[correctIdx] = array[correctIdx], array[i]
            continue
        i += 1
    return array


if __name__ == "__main__":
    print(cyclicSort([8, 3, 5, 9, 6, 2, 7, 1, 4]))
