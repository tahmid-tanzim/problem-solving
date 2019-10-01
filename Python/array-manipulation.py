#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://www.hackerrank.com/challenges/crush/problem


# def array_manipulation(n, queries):
#     operations = [0 for _ in range(n)]
#     for a, b, k in queries:
#         i = a - 1
#         while i < b:
#             operations[i] += k
#             i += 1
#     return max(operations)


if __name__ == '__main__':
    # print(array_manipulation(5, [
    #     [1, 1, 100],
    #     [2, 5, 100],
    #     [3, 4, 100]
    # ]))  # 200

    # print(array_manipulation(10, [
    #     [1, 5, 3],
    #     [4, 8, 7],
    #     [6, 9, 1]
    # ]))  # 10

    # print(array_manipulation(10, [
    #     [2, 6, 8],
    #     [3, 5, 7],
    #     [1, 8, 1],
    #     [5, 9, 15]
    # ]))  # 31

    operations_dictionary = [
        [(1, 3), 3],
        [(4, 7), 10],
        [(8, 11), 7],
        [(12, 13), 0]
    ]

    # operations_dictionary = {
    #     (1, 3): 3,
    #     (4, 7): 10,
    #     (8, 11): 7,
    #     (12, 13): 0
    # }

    '''
    Delete 
    1. (4, 7) -> 10,
    2. (8, 11) -> 7
    '''
    index = 1

    deleted_operations = [
        [(4, 7), 10],
        [(8, 11), 7]
    ]

    del operations_dictionary[index:len(deleted_operations) + index]

    '''
    Append 
    1. (4, 6) -> 10,
    2. (7, 7) -> 14,
    3. (8, 9) -> 11,
    4. (10, 11) -> 7
    '''
    updated_operations = [
        [(4, 6), 10],
        [(7, 7), 14],
        [(8, 9), 11],
        [(10, 11), 7]
    ]

    operations_dictionary[index:index] = updated_operations

    print(operations_dictionary)

    # for key in operations_dictionary:
    #     print("({}, {})".format(key[0], key[1]), ' -- ', operations_dictionary[key])
