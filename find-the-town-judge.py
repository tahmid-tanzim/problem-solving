#!/usr/bin/python3
# https://leetcode.com/problems/find-the-town-judge/
from typing import List


# def find_judge(n: int, trust: List[List[int]]) -> int:
#     """
#     I will track the town judge with people array of integer
#     In people array
#         value 0 in index (i) means i + 1 is town judge
#         value 1 in index (i) means i + 1 is a people trust another people
#         value 2 in index (i) means i + 1 is a people trust town judge
#
#     Case 1:
#     If n = 4 & people = [2, 2, 0, 2] then i == 2 is the town judge index.
#     So town judge number is index + 1 which is 3
#
#     Case 2:
#     If n = 3 & people = [2, 1, 0] Now i == 1 don't trust the town judge i == 2.
#     which doesn't satisfied the 2nd condition. So the result will be -1
#     """
#     people = [0] * n
#     for a, b in trust:
#         people[a - 1] = 1
#
#     try:
#         town_judge = people.index(0) + 1
#         for a, b in trust:
#             if b == town_judge:
#                 people[a - 1] += 1
#
#         return town_judge if people.count(2) == n - 1 else -1
#     except ValueError:
#         return -1


def find_judge(n: int, trust: List[List[int]]) -> int:
    people = [0] * n
    for a, b in trust:
        people[a - 1] -= 1
        people[b - 1] += 1

    try:
        town_judge = people.index(n - 1) + 1
        return town_judge
    except ValueError:
        return -1


if __name__ == "__main__":
    print(find_judge(2, [
        [1, 2]
    ]))  # 2

    print(find_judge(3, [
        [1, 3],
        [2, 3]
    ]))  # 3

    print(find_judge(3, [
        [1, 3],
        [2, 3],
        [3, 1]
    ]))  # -1

    print(find_judge(3, [
        [1, 2],
        [2, 3]
    ]))  # -1
