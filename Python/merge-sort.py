#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/merge-sorted-array/


def merge_sort(arr):
    size = len(arr)
    if size <= 1:
        return arr

    center = size // 2
    # Merge Left Array
    left_sorted_arr = merge_sort(arr[:center])
    # left_sorted_arr = arr[:center]
    # Merge Right Array
    right_sorted_arr = merge_sort(arr[center:])
    # right_sorted_arr = arr[center:]

    # Merge two array
    merged_array, i, j = [], 0, 0
    while i < len(left_sorted_arr) and j < len(right_sorted_arr):
        if left_sorted_arr[i] > right_sorted_arr[j]:
            merged_array.append(right_sorted_arr[j])
            j += 1
        elif left_sorted_arr[i] < right_sorted_arr[j]:
            merged_array.append(left_sorted_arr[i])
            i += 1
        else:
            merged_array.append(left_sorted_arr[i])
            i += 1
            merged_array.append(right_sorted_arr[j])
            j += 1

    if i != len(left_sorted_arr):
        merged_array += left_sorted_arr[i:]
    if j != len(right_sorted_arr):
        merged_array += right_sorted_arr[j:]
    return merged_array


if __name__ == '__main__':
    # print(merge_sort([1, 5, 6, 3, 8, 4, 7, 2, 4]))
    print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
    # print(merge_sort([1, 4, 5, 8, 2, 6, 7, 8, 9]))
    # merge_sort([1, 5, 6, 3, 8, 4, 7])
