#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/


def repeated_n_times(A):
    frequency = {}
    for a in A:
        if a in frequency:
            return a
        else:
            frequency[a] = 1


if __name__ == '__main__':
    print(repeated_n_times([1, 2, 3, 3]))
    print(repeated_n_times([2, 1, 2, 5, 3, 2]))
    print(repeated_n_times([5, 1, 5, 2, 5, 3, 5, 4]))
