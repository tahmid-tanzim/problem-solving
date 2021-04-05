#!/usr/bin/python3


def partition(array, index_list, p, r):
    pivot = array[r]
    left = p - 1
    right = p

    while right < r:
        if array[right] <= pivot:
            left += 1
            array[left], array[right] = array[right], array[left]
            index_list[left], index_list[right] = index_list[right], index_list[left]
        right += 1

    array[left + 1], array[r] = array[r], array[left + 1]
    index_list[left + 1], index_list[r] = index_list[r], index_list[left + 1]
    return left + 1


def quicksort(array, index_list, p, r):
    if p < r:
        q = partition(array, index_list, p, r)
        quicksort(array, index_list, p, q - 1)
        quicksort(array, index_list, q + 1, r)


def taskAssignment(k, tasks):
    tasks_index = list(range(2 * k))
    quicksort(tasks, tasks_index, 0, len(tasks) - 1)
    task_board = list()
    for i in range(k):
        task_board.append([tasks_index[i], tasks_index[2 * k - 1 - i]])
    return task_board


if __name__ == '__main__':
    print(f'Answer - {taskAssignment(3, [1, 3, 5, 3, 1, 4])}')
    # print(f'Answer - {taskAssignment(4, [2, 8, 7, 1, 3, 5, 6, 4])}')
