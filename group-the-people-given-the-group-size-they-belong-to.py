#!/usr/local/bin/python3.6

"""
https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
"""


def group_the_people(groupSizes):
    n = len(groupSizes)
    result, group = {}, []
    for ID in range(n):
        size = groupSizes[ID]
        if size in group:
            if len(group[size]) < size:
                group[size].append(ID)
            else:
                result.append(group[size])
                group[size] = [ID]
        else:
            group[size] = [ID]
    return result + list(group.values())


if __name__ == '__main__':
    print(group_the_people([3, 3, 3, 3, 3, 1, 3]))
    print(group_the_people([2, 1, 3, 3, 3, 2]))
