#!/usr/bin/python3


def index_all(search_list, target):
    indices = list()

    for i in range(len(search_list)):
        if search_list[i] == target:
            indices.append([i])
        elif isinstance(search_list[i], list):
            for index in index_all(search_list[i], target):
                indices.append([i] + index)
    return indices


if __name__ == "__main__":
    print(index_all(search_list=[
        [
            [1, 2, 3],
            2,
            [1, 3]
        ],
        [1, 2, 3]
    ], target=2))
