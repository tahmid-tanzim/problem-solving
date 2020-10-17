#!/Users/tahmid.tanzim/venv/bin/python3.7
from typing import List


def insert(arr: List[int], element: int):
    # Base Condition
    if len(arr) == 0 or arr[-1] <= element:
        arr.append(element)
        return arr

    last_element = arr[-1]
    insert(arr[:-1], last_element)
    arr.append(last_element)
    return arr


def sort_rc(arr: List[int]):
    # Base Condition
    if len(arr) == 1:
        return arr

    last_element = arr[-1]
    sort_rc(arr[:-1])
    insert(arr, last_element)
    # print('Sorted Array - ', arr, last_element)


if __name__ == '__main__':
    # sort_rc([4, 6, 3, 2, 5, 1])
    print(sort_rc([2, 3, 7, 6, 4, 5, 9]))

