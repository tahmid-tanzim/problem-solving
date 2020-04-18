#!/usr/local/bin/python3.6


def max_area(height) -> int:
    maximum_area = 0
    start_index = 0
    last_index = len(height) - 1

    while start_index < last_index:
        width = last_index - start_index
        if height[start_index] < height[last_index]:
            maximum_area = max(maximum_area, height[start_index] * width)
            start_index = start_index + 1
        else:
            maximum_area = max(maximum_area, height[last_index] * width)
            last_index = last_index - 1
    return maximum_area


if __name__ == '__main__':
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
