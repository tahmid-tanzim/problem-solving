#!/usr/bin/python3


def findSubsequence(array, idx, container):
    if idx >= len(array):
        print(container)
        return

    container.append(array[idx])
    findSubsequence(array, idx + 1, container)
    container.pop()
    findSubsequence(array, idx + 1, container)


def findSubsequenceSum(array, idx, container, total):
    if idx >= len(array):
        if total == 0:
            print(container)
        return

    container.append(array[idx])
    total -= array[idx]
    findSubsequenceSum(array, idx + 1, container, total)
    total += array[idx]
    container.pop()
    findSubsequenceSum(array, idx + 1, container, total)


def findOneSubsequenceSum(array, idx, container, total):
    if idx >= len(array):
        if total == 0:
            print(container)
            return True
        return False

    container.append(array[idx])
    total -= array[idx]
    found = findOneSubsequenceSum(array, idx + 1, container, total)
    if found:
        return True

    total += array[idx]
    container.pop()
    found = findOneSubsequenceSum(array, idx + 1, container, total)
    if found:
        return True

    return False


if __name__ == "__main__":
    # print(findSubsequence([3, 2, 1], 0, []))
    # print(findSubsequenceSum([1, 2, 1], 0, [], 2))
    print(findOneSubsequenceSum([1, 2, 1], 0, [], 2))
