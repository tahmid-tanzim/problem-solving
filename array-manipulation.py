#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://www.hackerrank.com/challenges/crush/problem


# def array_manipulation(n, queries):
#     operations_dictionary = [
#         [(1, n), 0]
#     ]
#     max_val = 0
#     for a, b, k in queries:
#         i = 0
#         index = 0
#         updated_operations, deleted_operations = [], []
#         while i < len(operations_dictionary):
#             [(lower, upper), total] = operations_dictionary[i]
#             if a <= b < lower <= upper:
#                 break
#             if lower <= a <= b <= upper:  # (a & b) In-between lower & upper boundary
#                 index = i
#                 deleted_operations.append([(lower, upper), total])
#                 if a == lower and b == upper:
#                     updated_operations.append([(lower, upper), total + k])
#                     max_val = max(max_val, total + k)
#                 if lower == a and b < upper:
#                     upper_diff = upper - b
#                     updated_operations.append([(a, b), total + k])
#                     updated_operations.append([(upper - upper_diff + 1, upper), total])
#                     max_val = max(max_val, total + k)
#                 if lower < a and b == upper:
#                     lower_diff = a - lower
#                     updated_operations.append([(lower, lower + lower_diff - 1), total])
#                     updated_operations.append([(a, b), total + k])
#                     max_val = max(max_val, total + k)
#                 if lower < a <= b < upper:
#                     lower_diff = a - lower
#                     upper_diff = upper - b
#                     updated_operations.append([(lower, lower + lower_diff - 1), total])
#                     updated_operations.append([(a, b), total + k])
#                     updated_operations.append([(upper - upper_diff + 1, upper), total])
#                     max_val = max(max_val, total + k)
#                 # print(i, "SE (a:{}, b: {})  lower: {} | upper {} | total {}".format(a, b, lower, upper, total))
#             else:  # (a & b) Outside lower & upper boundary
#                 if lower <= a <= upper < b:
#                     index = i
#                     deleted_operations.append([(lower, upper), total])
#                     if lower == a:  # == upper
#                         updated_operations.append([(lower, upper), total + k])
#                         max_val = max(max_val, total + k)
#                     if lower < a <= upper:
#                         lower_diff = a - lower
#                         updated_operations.append([(lower, lower + lower_diff - 1), total])
#                         updated_operations.append([(a, upper), total + k])
#                         max_val = max(max_val, total + k)
#                     # print(i, "S (a:{}, b: {})  lower: {} | upper {} | total {}".format(a, b, lower, upper, total))
#                 if a < lower <= upper < b:
#                     deleted_operations.append([(lower, upper), total])
#                     updated_operations.append([(lower, upper), total + k])
#                     max_val = max(max_val, total + k)
#                     # print(i, "M (a:{}, b: {})  lower: {} | upper {} | total {}".format(a, b, lower, upper, total))
#                 if a < lower <= b <= upper:
#                     deleted_operations.append([(lower, upper), total])
#                     if lower == b == upper:
#                         updated_operations.append([(lower, upper), total + k])
#                         max_val = max(max_val, total + k)
#                     if lower <= b < upper:
#                         upper_diff = upper - b
#                         updated_operations.append([(lower, b), total + k])
#                         updated_operations.append([(upper - upper_diff + 1, upper), total])
#                         max_val = max(max_val, total + k)
#                     # print(i, "E (a:{}, b: {})  lower: {} | upper {} | total {}".format(a, b, lower, upper, total))
#             i += 1
#         # print('deleted_operations: ', deleted_operations, index)
#         # print('updated_operations: ', updated_operations, index)
#         del operations_dictionary[index:len(deleted_operations) + index]
#         operations_dictionary[index:index] = updated_operations
#         # print('operations_dictionary: ', operations_dictionary, max_val)
#     return max_val


# def array_manipulation(n, queries):
#     operations = [0 for _ in range(n)]
#     for a, b, k in queries:
#         i = a - 1
#         while i < b:
#             operations[i] += k
#             i += 1
#     return max(operations)
from collections import Counter


def array_manipulation(n, queries):
    c = Counter()
    for a, b, k in queries:
        c[a] += k
        c[b + 1] -= k

    arr_sum = 0
    max_sum = 0

    for i in sorted(c)[:-1]:
        arr_sum += c[i]
        max_sum = max(max_sum, arr_sum)
    return max_sum


if __name__ == '__main__':
    # print(array_manipulation(5, [
    #     [1, 1, 100],
    #     [2, 5, 100],
    #     [3, 4, 100]
    # ]))  # 200

    print(array_manipulation(10, [
        [1, 5, 3],
        [4, 8, 7],
        [6, 9, 1]
    ]))  # 10

    # print(array_manipulation(10, [
    #     [2, 6, 8],
    #     [3, 5, 7],
    #     [1, 8, 1],
    #     [5, 9, 15]
    # ]))  # 31

    # operations_dictionary = [
    #     [(1, 3), 3],
    #     [(4, 7), 10],
    #     [(8, 11), 7],
    #     [(12, 15), 0]
    # ]

    '''
    Delete 
    1. (4, 7) -> 10,
    2. (8, 11) -> 7
    '''
    # index = 1
    #
    # deleted_operations = [
    #     [(4, 7), 10],
    #     [(8, 11), 7]
    # ]
    #
    # del operations_dictionary[index:len(deleted_operations) + index]

    '''
    Append 
    a = 7
    b = 9
    k = 4
    1. (4, 6) -> 10,
    2. (7, 7) -> 14,
    3. (8, 9) -> 11,
    4. (10, 11) -> 7
    '''
    # updated_operations = [
    #     [(4, 6), 10],
    #     [(7, 7), 14],
    #     [(8, 9), 11],
    #     [(10, 11), 7]
    # ]
    #
    # operations_dictionary[index:index] = updated_operations
    #
    # print(operations_dictionary)

    # i = 0
    # a = 7
    # b = 9
    # k = 4
    # index = 0
    # updated_operations, deleted_operations = [], []
    # while i < len(operations_dictionary):
    #     [(lower, upper), total] = operations_dictionary[i]
    #     if a <= b < lower <= upper:
    #         break
    #     if lower <= a <= b <= upper:  # (a & b) In-between lower & upper boundary
    #         index = i
    #         deleted_operations.append([(lower, upper), total])
    #         if a == lower and b == upper:
    #             updated_operations.append([(lower, upper), total + k])
    #         if lower == a and b < upper:
    #             upper_diff = upper - b
    #             updated_operations.append([(a, b), total + k])
    #             updated_operations.append([(upper - upper_diff + 1, upper), total])
    #         if lower < a and b == upper:
    #             lower_diff = a - lower
    #             updated_operations.append([(lower, lower + lower_diff - 1), total])
    #             updated_operations.append([(a, b), total + k])
    #         if lower < a <= b < upper:
    #             lower_diff = a - lower
    #             upper_diff = upper - b
    #             updated_operations.append([(lower, lower + lower_diff - 1), total])
    #             updated_operations.append([(a, b), total + k])
    #             updated_operations.append([(upper - upper_diff + 1, upper), total])
    #         print(i, "SE (a:{}, b: {})  lower: {} | upper {} | total {}".format(a, b, lower, upper, total))
    #     else:  # (a & b) Outside lower & upper boundary
    #         if lower <= a <= upper < b:
    #             index = i
    #             deleted_operations.append([(lower, upper), total])
    #             if lower == a == upper:
    #                 updated_operations.append([(lower, upper), total + k])
    #             if lower < a <= upper:
    #                 lower_diff = a - lower
    #                 updated_operations.append([(lower, lower + lower_diff - 1), total])
    #                 updated_operations.append([(a, upper), total + k])
    #             print(i, "S (a:{}, b: {})  lower: {} | upper {} | total {}".format(a, b, lower, upper, total))
    #         if a < lower <= upper < b:
    #             deleted_operations.append([(lower, upper), total])
    #             updated_operations.append([(lower, upper), total + k])
    #             print(i, "M (a:{}, b: {})  lower: {} | upper {} | total {}".format(a, b, lower, upper, total))
    #         if a < lower <= b <= upper:
    #             deleted_operations.append([(lower, upper), total])
    #             if lower == b == upper:
    #                 updated_operations.append([(lower, upper), total + k])
    #             if lower <= b < upper:
    #                 upper_diff = upper - b
    #                 updated_operations.append([(lower, b), total + k])
    #                 updated_operations.append([(upper - upper_diff + 1, upper), total])
    #             print(i, "E (a:{}, b: {})  lower: {} | upper {} | total {}".format(a, b, lower, upper, total))
    #     i += 1
    # print('deleted_operations: ', deleted_operations, index)
    # print('updated_operations: ', updated_operations, index)
