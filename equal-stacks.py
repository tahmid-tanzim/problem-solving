#!/Users/tahmid.tanzim/venv/bin/python3.7
# https://www.hackerrank.com/challenges/equal-stacks/problem


# def equal_stacks(h1, h2, h3):
#     height = [h1, h2, h3]
#     total = [sum(h1), sum(h2), sum(h3)]
#     head_index = [0, 0, 0]
#     while not len(set(total)) <= 1:
#         min_index = total.index(min(total))
#
#         if min_index == 2:
#             d0, d1 = total[0] - total[min_index], total[1] - total[min_index]
#             s0, s1, = 0, 0
#
#             while d0 > s0:
#                 if head_index[0] == len(height[0]):
#                     return 0
#                 s0 += height[0][head_index[0]]
#                 head_index[0] += 1
#             total[0] -= s0
#
#             while d1 > s1:
#                 if head_index[1] == len(height[1]):
#                     return 0
#                 s1 += height[1][head_index[1]]
#                 head_index[1] += 1
#             total[1] -= s1
#
#         elif min_index == 1:
#             d0, d2 = total[0] - total[min_index], total[2] - total[min_index]
#             s0, s2, = 0, 0
#
#             while d0 > s0:
#                 if head_index[0] == len(height[0]):
#                     return 0
#                 s0 += height[0][head_index[0]]
#                 head_index[0] += 1
#             total[0] -= s0
#
#             while d2 > s2:
#                 if head_index[2] == len(height[2]):
#                     return 0
#                 s2 += height[2][head_index[2]]
#                 head_index[2] += 1
#             total[2] -= s2
#
#         else:
#             d2, d1 = total[2] - total[min_index], total[1] - total[min_index]
#             s2, s1, = 0, 0
#
#             while d2 > s2:
#                 if head_index[2] == len(height[2]):
#                     return 0
#                 s2 += height[2][head_index[2]]
#                 head_index[2] += 1
#             total[2] -= s2
#
#             while d1 > s1:
#                 if head_index[1] == len(height[1]):
#                     return 0
#                 s1 += height[1][head_index[1]]
#                 head_index[1] += 1
#             total[1] -= s1
#
#     return total[0]


def equal_stacks(h1, h2, h3):
    height = [h1, h2, h3]
    total = [sum(h1), sum(h2), sum(h3)]
    head_index = [0, 0, 0]
    while not len(set(total)) <= 1:
        min_index = total.index(min(total))
        for x in range(3):
            if x is not min_index:
                diff = total[x] - total[min_index]
                count = 0
                while diff > count:
                    if head_index[x] == len(height[x]):
                        return 0
                    count += height[x][head_index[x]]
                    head_index[x] += 1
                total[x] -= count
    return total[0]


if __name__ == '__main__':
    print(equal_stacks([3, 2, 1, 1, 1], [4, 3, 2], [1, 1, 4, 1]))
