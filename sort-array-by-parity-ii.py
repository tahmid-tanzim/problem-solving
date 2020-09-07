#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/sort-array-by-parity-ii/


def sort_array_by_parity_ii(A):
    even, odd, output = 0, 1, [0] * len(A)
    for a in A:
        if a % 2 == 0:
            output[even] = a
            even += 2
        else:
            output[odd] = a
            odd += 2
    return output


if __name__ == '__main__':
    print(sort_array_by_parity_ii([4, 2, 1, 0, 5, 7]))
