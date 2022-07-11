#!/usr/bin/python3


def subsequence(array, idx, container):
    if idx >= len(array):
        print(container)
        return

    container.append(array[idx])
    subsequence(array, idx + 1, container)
    container.pop()
    subsequence(array, idx + 1, container)


if __name__ == "__main__":
    print(subsequence([3, 2, 1], 0, []))
