#!/usr/bin/python3


def partition(array, p, r):
    pivot = array[r]
    left = p - 1
    right = p

    while right < r:
        if array[right] <= pivot:
            left += 1
            array[left], array[right] = array[right], array[left]
        right += 1

    array[left + 1], array[r] = array[r], array[left + 1]
    return left + 1


def quicksort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quicksort(array, p, q - 1)
        quicksort(array, q + 1, r)


if __name__ == '__main__':
    array = [1, 3, 5, 3, 1, 4]
    quicksort(array, 0, len(array) - 1)
    print(f'Answer - {array}')
