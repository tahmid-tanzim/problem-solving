#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions
# transposed


if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4, 6],
        [5, 6, 7, 8, 9],
        [9, 10, 11, 12, 3],
    ]

    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print(transposed)
