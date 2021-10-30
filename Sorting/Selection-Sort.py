#!/usr/bin/python3
# https://www.algoexpert.io/questions/Selection%20Sort


# Best, Avg. & Worst Time Complexity - O(n^2), Space Complexity - O(1)
def selectionSort(array):
    n = len(array)
    for arrow in range(n - 1):
        min_item = {
            'index': arrow,
            'value': array[arrow]
        }
        i = arrow + 1
        while i < n:
            if array[i] < min_item['value']:
                min_item = {
                    'index': i,
                    'value': array[i]
                }
            i += 1
        # Swap
        array[arrow], array[min_item['index']] = array[min_item['index']], array[arrow]
    return array


if __name__ == "__main__":
    print(selectionSort([8, 5, 2, 9, 5, 6, 3]))
