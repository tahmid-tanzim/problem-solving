#!/usr/local/bin/python3.6

"""
https://leetcode.com/problems/destination-city/
"""


def dest_city(paths):
    first = paths.pop(0)
    path = {'FROM': [first[0]], 'TO': [first[1]]}
    for [start, end] in paths:
        try:
            path['TO'].remove(start)
        except ValueError:
            path['FROM'].append(start)
        try:
            path['FROM'].remove(end)
        except ValueError:
            path['TO'].append(end)
    return path['TO'][0]


# def dest_city(paths):
#     path = {
#         'FROM': [paths[0][0]],
#         'TO': [paths[0][1]]
#     }
#     n = len(paths)
#     for i in range(1, n):
#         [start, end] = paths[i]
#         if start in path['TO']:
#             path['TO'].remove(start)
#         else:
#             path['FROM'].append(start)
#         if end in path['FROM']:
#             path['FROM'].remove(end)
#         else:
#             path['TO'].append(end)
#     return path['TO'][0]


if __name__ == '__main__':
    print(dest_city([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
    print(dest_city([["B", "C"], ["D", "B"], ["C", "A"]]))
    print(dest_city([["A", "Z"]]))
